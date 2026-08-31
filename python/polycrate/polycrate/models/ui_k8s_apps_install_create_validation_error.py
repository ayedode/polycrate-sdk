from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.ui_k8s_apps_install_create_active_error_component import UiK8SAppsInstallCreateActiveErrorComponent
    from ..models.ui_k8s_apps_install_create_actual_availability_error_component import (
        UiK8SAppsInstallCreateActualAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_annotations_error_component import (
        UiK8SAppsInstallCreateAnnotationsErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_archived_at_error_component import (
        UiK8SAppsInstallCreateArchivedAtErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_archived_by_error_component import (
        UiK8SAppsInstallCreateArchivedByErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_archived_error_component import (
        UiK8SAppsInstallCreateArchivedErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_archived_reason_error_component import (
        UiK8SAppsInstallCreateArchivedReasonErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_artifact_error_component import (
        UiK8SAppsInstallCreateArtifactErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_artifact_package_error_component import (
        UiK8SAppsInstallCreateArtifactPackageErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_block_error_component import UiK8SAppsInstallCreateBlockErrorComponent
    from ..models.ui_k8s_apps_install_create_byoa_error_component import UiK8SAppsInstallCreateByoaErrorComponent
    from ..models.ui_k8s_apps_install_create_catalogue_app_error_component import (
        UiK8SAppsInstallCreateCatalogueAppErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_created_by_component_error_component import (
        UiK8SAppsInstallCreateCreatedByComponentErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_created_by_user_error_component import (
        UiK8SAppsInstallCreateCreatedByUserErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_criticality_error_component import (
        UiK8SAppsInstallCreateCriticalityErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_debug_mode_error_component import (
        UiK8SAppsInstallCreateDebugModeErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_description_error_component import (
        UiK8SAppsInstallCreateDescriptionErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_discovery_enabled_error_component import (
        UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_display_name_error_component import (
        UiK8SAppsInstallCreateDisplayNameErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_excluded_from_downtime_until_error_component import (
        UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_ha_enabled_error_component import (
        UiK8SAppsInstallCreateHaEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_helm_chart_error_component import (
        UiK8SAppsInstallCreateHelmChartErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_installation_failed_error_component import (
        UiK8SAppsInstallCreateInstallationFailedErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_installation_running_error_component import (
        UiK8SAppsInstallCreateInstallationRunningErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_installed_error_component import (
        UiK8SAppsInstallCreateInstalledErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_installed_version_error_component import (
        UiK8SAppsInstallCreateInstalledVersionErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_k8s_cluster_error_component import (
        UiK8SAppsInstallCreateK8SClusterErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_kind_error_component import UiK8SAppsInstallCreateKindErrorComponent
    from ..models.ui_k8s_apps_install_create_labels_error_component import UiK8SAppsInstallCreateLabelsErrorComponent
    from ..models.ui_k8s_apps_install_create_last_installation_error_component import (
        UiK8SAppsInstallCreateLastInstallationErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_last_metrics_check_error_component import (
        UiK8SAppsInstallCreateLastMetricsCheckErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component import (
        UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_managed_by_content_type_error_component import (
        UiK8SAppsInstallCreateManagedByContentTypeErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_managed_by_object_id_error_component import (
        UiK8SAppsInstallCreateManagedByObjectIdErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_modified_by_user_error_component import (
        UiK8SAppsInstallCreateModifiedByUserErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_name_error_component import UiK8SAppsInstallCreateNameErrorComponent
    from ..models.ui_k8s_apps_install_create_namespace_error_component import (
        UiK8SAppsInstallCreateNamespaceErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_non_field_errors_error_component import (
        UiK8SAppsInstallCreateNonFieldErrorsErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_platform_dns_record_created_error_component import (
        UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_platform_service_error_component import (
        UiK8SAppsInstallCreatePlatformServiceErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_available_error_component import (
        UiK8SAppsInstallCreatePodsAvailableErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_details_error_component import (
        UiK8SAppsInstallCreatePodsDetailsErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_ready_error_component import (
        UiK8SAppsInstallCreatePodsReadyErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_restart_count_last_hour_error_component import (
        UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_restart_count_total_error_component import (
        UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_status_hash_error_component import (
        UiK8SAppsInstallCreatePodsStatusHashErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_status_updated_at_error_component import (
        UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_total_error_component import (
        UiK8SAppsInstallCreatePodsTotalErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_pods_unavailable_error_component import (
        UiK8SAppsInstallCreatePodsUnavailableErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_provider_error_component import (
        UiK8SAppsInstallCreateProviderErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_provider_id_error_component import (
        UiK8SAppsInstallCreateProviderIdErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_provider_reference_error_component import (
        UiK8SAppsInstallCreateProviderReferenceErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_reconciliation_enabled_error_component import (
        UiK8SAppsInstallCreateReconciliationEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_scope_error_component import UiK8SAppsInstallCreateScopeErrorComponent
    from ..models.ui_k8s_apps_install_create_sla_availability_error_component import (
        UiK8SAppsInstallCreateSlaAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_sla_target_error_component import (
        UiK8SAppsInstallCreateSlaTargetErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_sla_window_days_error_component import (
        UiK8SAppsInstallCreateSlaWindowDaysErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_slo_availability_error_component import (
        UiK8SAppsInstallCreateSloAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_slo_target_error_component import (
        UiK8SAppsInstallCreateSloTargetErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_slo_window_days_error_component import (
        UiK8SAppsInstallCreateSloWindowDaysErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_source_error_component import UiK8SAppsInstallCreateSourceErrorComponent
    from ..models.ui_k8s_apps_install_create_target_availability_error_component import (
        UiK8SAppsInstallCreateTargetAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_uninstallation_failed_error_component import (
        UiK8SAppsInstallCreateUninstallationFailedErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_uninstallation_running_error_component import (
        UiK8SAppsInstallCreateUninstallationRunningErrorComponent,
    )
    from ..models.ui_k8s_apps_install_create_uninstalled_error_component import (
        UiK8SAppsInstallCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="UiK8SAppsInstallCreateValidationError")


@_attrs_define
class UiK8SAppsInstallCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[UiK8SAppsInstallCreateActiveErrorComponent | UiK8SAppsInstallCreateActualAvailabilityErrorComponent
            | UiK8SAppsInstallCreateAnnotationsErrorComponent | UiK8SAppsInstallCreateArchivedAtErrorComponent |
            UiK8SAppsInstallCreateArchivedByErrorComponent | UiK8SAppsInstallCreateArchivedErrorComponent |
            UiK8SAppsInstallCreateArchivedReasonErrorComponent | UiK8SAppsInstallCreateArtifactErrorComponent |
            UiK8SAppsInstallCreateArtifactPackageErrorComponent | UiK8SAppsInstallCreateBlockErrorComponent |
            UiK8SAppsInstallCreateByoaErrorComponent | UiK8SAppsInstallCreateCatalogueAppErrorComponent |
            UiK8SAppsInstallCreateCreatedByComponentErrorComponent | UiK8SAppsInstallCreateCreatedByUserErrorComponent |
            UiK8SAppsInstallCreateCriticalityErrorComponent | UiK8SAppsInstallCreateDebugModeErrorComponent |
            UiK8SAppsInstallCreateDescriptionErrorComponent | UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent |
            UiK8SAppsInstallCreateDisplayNameErrorComponent | UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent
            | UiK8SAppsInstallCreateHaEnabledErrorComponent | UiK8SAppsInstallCreateHelmChartErrorComponent |
            UiK8SAppsInstallCreateInstallationFailedErrorComponent | UiK8SAppsInstallCreateInstallationRunningErrorComponent
            | UiK8SAppsInstallCreateInstalledErrorComponent | UiK8SAppsInstallCreateInstalledVersionErrorComponent |
            UiK8SAppsInstallCreateK8SClusterErrorComponent | UiK8SAppsInstallCreateKindErrorComponent |
            UiK8SAppsInstallCreateLabelsErrorComponent | UiK8SAppsInstallCreateLastInstallationErrorComponent |
            UiK8SAppsInstallCreateLastMetricsCheckErrorComponent |
            UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent |
            UiK8SAppsInstallCreateManagedByContentTypeErrorComponent | UiK8SAppsInstallCreateManagedByObjectIdErrorComponent
            | UiK8SAppsInstallCreateModifiedByUserErrorComponent | UiK8SAppsInstallCreateNameErrorComponent |
            UiK8SAppsInstallCreateNamespaceErrorComponent | UiK8SAppsInstallCreateNonFieldErrorsErrorComponent |
            UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent |
            UiK8SAppsInstallCreatePlatformServiceErrorComponent | UiK8SAppsInstallCreatePodsAvailableErrorComponent |
            UiK8SAppsInstallCreatePodsDetailsErrorComponent | UiK8SAppsInstallCreatePodsReadyErrorComponent |
            UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent |
            UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent | UiK8SAppsInstallCreatePodsStatusHashErrorComponent |
            UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent | UiK8SAppsInstallCreatePodsTotalErrorComponent |
            UiK8SAppsInstallCreatePodsUnavailableErrorComponent | UiK8SAppsInstallCreateProviderErrorComponent |
            UiK8SAppsInstallCreateProviderIdErrorComponent | UiK8SAppsInstallCreateProviderReferenceErrorComponent |
            UiK8SAppsInstallCreateReconciliationEnabledErrorComponent | UiK8SAppsInstallCreateScopeErrorComponent |
            UiK8SAppsInstallCreateSlaAvailabilityErrorComponent | UiK8SAppsInstallCreateSlaTargetErrorComponent |
            UiK8SAppsInstallCreateSlaWindowDaysErrorComponent | UiK8SAppsInstallCreateSloAvailabilityErrorComponent |
            UiK8SAppsInstallCreateSloTargetErrorComponent | UiK8SAppsInstallCreateSloWindowDaysErrorComponent |
            UiK8SAppsInstallCreateSourceErrorComponent | UiK8SAppsInstallCreateTargetAvailabilityErrorComponent |
            UiK8SAppsInstallCreateUninstallationFailedErrorComponent |
            UiK8SAppsInstallCreateUninstallationRunningErrorComponent | UiK8SAppsInstallCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        UiK8SAppsInstallCreateActiveErrorComponent
        | UiK8SAppsInstallCreateActualAvailabilityErrorComponent
        | UiK8SAppsInstallCreateAnnotationsErrorComponent
        | UiK8SAppsInstallCreateArchivedAtErrorComponent
        | UiK8SAppsInstallCreateArchivedByErrorComponent
        | UiK8SAppsInstallCreateArchivedErrorComponent
        | UiK8SAppsInstallCreateArchivedReasonErrorComponent
        | UiK8SAppsInstallCreateArtifactErrorComponent
        | UiK8SAppsInstallCreateArtifactPackageErrorComponent
        | UiK8SAppsInstallCreateBlockErrorComponent
        | UiK8SAppsInstallCreateByoaErrorComponent
        | UiK8SAppsInstallCreateCatalogueAppErrorComponent
        | UiK8SAppsInstallCreateCreatedByComponentErrorComponent
        | UiK8SAppsInstallCreateCreatedByUserErrorComponent
        | UiK8SAppsInstallCreateCriticalityErrorComponent
        | UiK8SAppsInstallCreateDebugModeErrorComponent
        | UiK8SAppsInstallCreateDescriptionErrorComponent
        | UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent
        | UiK8SAppsInstallCreateDisplayNameErrorComponent
        | UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent
        | UiK8SAppsInstallCreateHaEnabledErrorComponent
        | UiK8SAppsInstallCreateHelmChartErrorComponent
        | UiK8SAppsInstallCreateInstallationFailedErrorComponent
        | UiK8SAppsInstallCreateInstallationRunningErrorComponent
        | UiK8SAppsInstallCreateInstalledErrorComponent
        | UiK8SAppsInstallCreateInstalledVersionErrorComponent
        | UiK8SAppsInstallCreateK8SClusterErrorComponent
        | UiK8SAppsInstallCreateKindErrorComponent
        | UiK8SAppsInstallCreateLabelsErrorComponent
        | UiK8SAppsInstallCreateLastInstallationErrorComponent
        | UiK8SAppsInstallCreateLastMetricsCheckErrorComponent
        | UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent
        | UiK8SAppsInstallCreateManagedByContentTypeErrorComponent
        | UiK8SAppsInstallCreateManagedByObjectIdErrorComponent
        | UiK8SAppsInstallCreateModifiedByUserErrorComponent
        | UiK8SAppsInstallCreateNameErrorComponent
        | UiK8SAppsInstallCreateNamespaceErrorComponent
        | UiK8SAppsInstallCreateNonFieldErrorsErrorComponent
        | UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent
        | UiK8SAppsInstallCreatePlatformServiceErrorComponent
        | UiK8SAppsInstallCreatePodsAvailableErrorComponent
        | UiK8SAppsInstallCreatePodsDetailsErrorComponent
        | UiK8SAppsInstallCreatePodsReadyErrorComponent
        | UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent
        | UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent
        | UiK8SAppsInstallCreatePodsStatusHashErrorComponent
        | UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent
        | UiK8SAppsInstallCreatePodsTotalErrorComponent
        | UiK8SAppsInstallCreatePodsUnavailableErrorComponent
        | UiK8SAppsInstallCreateProviderErrorComponent
        | UiK8SAppsInstallCreateProviderIdErrorComponent
        | UiK8SAppsInstallCreateProviderReferenceErrorComponent
        | UiK8SAppsInstallCreateReconciliationEnabledErrorComponent
        | UiK8SAppsInstallCreateScopeErrorComponent
        | UiK8SAppsInstallCreateSlaAvailabilityErrorComponent
        | UiK8SAppsInstallCreateSlaTargetErrorComponent
        | UiK8SAppsInstallCreateSlaWindowDaysErrorComponent
        | UiK8SAppsInstallCreateSloAvailabilityErrorComponent
        | UiK8SAppsInstallCreateSloTargetErrorComponent
        | UiK8SAppsInstallCreateSloWindowDaysErrorComponent
        | UiK8SAppsInstallCreateSourceErrorComponent
        | UiK8SAppsInstallCreateTargetAvailabilityErrorComponent
        | UiK8SAppsInstallCreateUninstallationFailedErrorComponent
        | UiK8SAppsInstallCreateUninstallationRunningErrorComponent
        | UiK8SAppsInstallCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_k8s_apps_install_create_active_error_component import (
            UiK8SAppsInstallCreateActiveErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_actual_availability_error_component import (
            UiK8SAppsInstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_annotations_error_component import (
            UiK8SAppsInstallCreateAnnotationsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_at_error_component import (
            UiK8SAppsInstallCreateArchivedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_by_error_component import (
            UiK8SAppsInstallCreateArchivedByErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_error_component import (
            UiK8SAppsInstallCreateArchivedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_reason_error_component import (
            UiK8SAppsInstallCreateArchivedReasonErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_artifact_error_component import (
            UiK8SAppsInstallCreateArtifactErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_artifact_package_error_component import (
            UiK8SAppsInstallCreateArtifactPackageErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_block_error_component import UiK8SAppsInstallCreateBlockErrorComponent
        from ..models.ui_k8s_apps_install_create_byoa_error_component import UiK8SAppsInstallCreateByoaErrorComponent
        from ..models.ui_k8s_apps_install_create_catalogue_app_error_component import (
            UiK8SAppsInstallCreateCatalogueAppErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_created_by_component_error_component import (
            UiK8SAppsInstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_created_by_user_error_component import (
            UiK8SAppsInstallCreateCreatedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_criticality_error_component import (
            UiK8SAppsInstallCreateCriticalityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_debug_mode_error_component import (
            UiK8SAppsInstallCreateDebugModeErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_description_error_component import (
            UiK8SAppsInstallCreateDescriptionErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_discovery_enabled_error_component import (
            UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_display_name_error_component import (
            UiK8SAppsInstallCreateDisplayNameErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_excluded_from_downtime_until_error_component import (
            UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_ha_enabled_error_component import (
            UiK8SAppsInstallCreateHaEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_helm_chart_error_component import (
            UiK8SAppsInstallCreateHelmChartErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installation_failed_error_component import (
            UiK8SAppsInstallCreateInstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installation_running_error_component import (
            UiK8SAppsInstallCreateInstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installed_error_component import (
            UiK8SAppsInstallCreateInstalledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installed_version_error_component import (
            UiK8SAppsInstallCreateInstalledVersionErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_kind_error_component import UiK8SAppsInstallCreateKindErrorComponent
        from ..models.ui_k8s_apps_install_create_labels_error_component import (
            UiK8SAppsInstallCreateLabelsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_installation_error_component import (
            UiK8SAppsInstallCreateLastInstallationErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_metrics_check_error_component import (
            UiK8SAppsInstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component import (
            UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_managed_by_content_type_error_component import (
            UiK8SAppsInstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_managed_by_object_id_error_component import (
            UiK8SAppsInstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_modified_by_user_error_component import (
            UiK8SAppsInstallCreateModifiedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_name_error_component import UiK8SAppsInstallCreateNameErrorComponent
        from ..models.ui_k8s_apps_install_create_namespace_error_component import (
            UiK8SAppsInstallCreateNamespaceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_non_field_errors_error_component import (
            UiK8SAppsInstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_platform_dns_record_created_error_component import (
            UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_platform_service_error_component import (
            UiK8SAppsInstallCreatePlatformServiceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_available_error_component import (
            UiK8SAppsInstallCreatePodsAvailableErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_details_error_component import (
            UiK8SAppsInstallCreatePodsDetailsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_ready_error_component import (
            UiK8SAppsInstallCreatePodsReadyErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_restart_count_last_hour_error_component import (
            UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_restart_count_total_error_component import (
            UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_status_hash_error_component import (
            UiK8SAppsInstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_status_updated_at_error_component import (
            UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_total_error_component import (
            UiK8SAppsInstallCreatePodsTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_unavailable_error_component import (
            UiK8SAppsInstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_error_component import (
            UiK8SAppsInstallCreateProviderErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_id_error_component import (
            UiK8SAppsInstallCreateProviderIdErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_reference_error_component import (
            UiK8SAppsInstallCreateProviderReferenceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_reconciliation_enabled_error_component import (
            UiK8SAppsInstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_scope_error_component import UiK8SAppsInstallCreateScopeErrorComponent
        from ..models.ui_k8s_apps_install_create_sla_availability_error_component import (
            UiK8SAppsInstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_sla_target_error_component import (
            UiK8SAppsInstallCreateSlaTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_sla_window_days_error_component import (
            UiK8SAppsInstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_availability_error_component import (
            UiK8SAppsInstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_target_error_component import (
            UiK8SAppsInstallCreateSloTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_window_days_error_component import (
            UiK8SAppsInstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_source_error_component import (
            UiK8SAppsInstallCreateSourceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_target_availability_error_component import (
            UiK8SAppsInstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstallation_failed_error_component import (
            UiK8SAppsInstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstallation_running_error_component import (
            UiK8SAppsInstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstalled_error_component import (
            UiK8SAppsInstallCreateUninstalledErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, UiK8SAppsInstallCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsInstallCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_k8s_apps_install_create_active_error_component import (
            UiK8SAppsInstallCreateActiveErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_actual_availability_error_component import (
            UiK8SAppsInstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_annotations_error_component import (
            UiK8SAppsInstallCreateAnnotationsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_at_error_component import (
            UiK8SAppsInstallCreateArchivedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_by_error_component import (
            UiK8SAppsInstallCreateArchivedByErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_error_component import (
            UiK8SAppsInstallCreateArchivedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_archived_reason_error_component import (
            UiK8SAppsInstallCreateArchivedReasonErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_artifact_error_component import (
            UiK8SAppsInstallCreateArtifactErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_artifact_package_error_component import (
            UiK8SAppsInstallCreateArtifactPackageErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_block_error_component import UiK8SAppsInstallCreateBlockErrorComponent
        from ..models.ui_k8s_apps_install_create_byoa_error_component import UiK8SAppsInstallCreateByoaErrorComponent
        from ..models.ui_k8s_apps_install_create_catalogue_app_error_component import (
            UiK8SAppsInstallCreateCatalogueAppErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_created_by_component_error_component import (
            UiK8SAppsInstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_created_by_user_error_component import (
            UiK8SAppsInstallCreateCreatedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_criticality_error_component import (
            UiK8SAppsInstallCreateCriticalityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_debug_mode_error_component import (
            UiK8SAppsInstallCreateDebugModeErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_description_error_component import (
            UiK8SAppsInstallCreateDescriptionErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_discovery_enabled_error_component import (
            UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_display_name_error_component import (
            UiK8SAppsInstallCreateDisplayNameErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_excluded_from_downtime_until_error_component import (
            UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_ha_enabled_error_component import (
            UiK8SAppsInstallCreateHaEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_helm_chart_error_component import (
            UiK8SAppsInstallCreateHelmChartErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installation_failed_error_component import (
            UiK8SAppsInstallCreateInstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installation_running_error_component import (
            UiK8SAppsInstallCreateInstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installed_error_component import (
            UiK8SAppsInstallCreateInstalledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_installed_version_error_component import (
            UiK8SAppsInstallCreateInstalledVersionErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_k8s_cluster_error_component import (
            UiK8SAppsInstallCreateK8SClusterErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_kind_error_component import UiK8SAppsInstallCreateKindErrorComponent
        from ..models.ui_k8s_apps_install_create_labels_error_component import (
            UiK8SAppsInstallCreateLabelsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_installation_error_component import (
            UiK8SAppsInstallCreateLastInstallationErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_metrics_check_error_component import (
            UiK8SAppsInstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component import (
            UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_managed_by_content_type_error_component import (
            UiK8SAppsInstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_managed_by_object_id_error_component import (
            UiK8SAppsInstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_modified_by_user_error_component import (
            UiK8SAppsInstallCreateModifiedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_name_error_component import UiK8SAppsInstallCreateNameErrorComponent
        from ..models.ui_k8s_apps_install_create_namespace_error_component import (
            UiK8SAppsInstallCreateNamespaceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_non_field_errors_error_component import (
            UiK8SAppsInstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_platform_dns_record_created_error_component import (
            UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_platform_service_error_component import (
            UiK8SAppsInstallCreatePlatformServiceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_available_error_component import (
            UiK8SAppsInstallCreatePodsAvailableErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_details_error_component import (
            UiK8SAppsInstallCreatePodsDetailsErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_ready_error_component import (
            UiK8SAppsInstallCreatePodsReadyErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_restart_count_last_hour_error_component import (
            UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_restart_count_total_error_component import (
            UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_status_hash_error_component import (
            UiK8SAppsInstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_status_updated_at_error_component import (
            UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_total_error_component import (
            UiK8SAppsInstallCreatePodsTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_pods_unavailable_error_component import (
            UiK8SAppsInstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_error_component import (
            UiK8SAppsInstallCreateProviderErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_id_error_component import (
            UiK8SAppsInstallCreateProviderIdErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_provider_reference_error_component import (
            UiK8SAppsInstallCreateProviderReferenceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_reconciliation_enabled_error_component import (
            UiK8SAppsInstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_scope_error_component import UiK8SAppsInstallCreateScopeErrorComponent
        from ..models.ui_k8s_apps_install_create_sla_availability_error_component import (
            UiK8SAppsInstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_sla_target_error_component import (
            UiK8SAppsInstallCreateSlaTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_sla_window_days_error_component import (
            UiK8SAppsInstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_availability_error_component import (
            UiK8SAppsInstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_target_error_component import (
            UiK8SAppsInstallCreateSloTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_slo_window_days_error_component import (
            UiK8SAppsInstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_source_error_component import (
            UiK8SAppsInstallCreateSourceErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_target_availability_error_component import (
            UiK8SAppsInstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstallation_failed_error_component import (
            UiK8SAppsInstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstallation_running_error_component import (
            UiK8SAppsInstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_install_create_uninstalled_error_component import (
            UiK8SAppsInstallCreateUninstalledErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                UiK8SAppsInstallCreateActiveErrorComponent
                | UiK8SAppsInstallCreateActualAvailabilityErrorComponent
                | UiK8SAppsInstallCreateAnnotationsErrorComponent
                | UiK8SAppsInstallCreateArchivedAtErrorComponent
                | UiK8SAppsInstallCreateArchivedByErrorComponent
                | UiK8SAppsInstallCreateArchivedErrorComponent
                | UiK8SAppsInstallCreateArchivedReasonErrorComponent
                | UiK8SAppsInstallCreateArtifactErrorComponent
                | UiK8SAppsInstallCreateArtifactPackageErrorComponent
                | UiK8SAppsInstallCreateBlockErrorComponent
                | UiK8SAppsInstallCreateByoaErrorComponent
                | UiK8SAppsInstallCreateCatalogueAppErrorComponent
                | UiK8SAppsInstallCreateCreatedByComponentErrorComponent
                | UiK8SAppsInstallCreateCreatedByUserErrorComponent
                | UiK8SAppsInstallCreateCriticalityErrorComponent
                | UiK8SAppsInstallCreateDebugModeErrorComponent
                | UiK8SAppsInstallCreateDescriptionErrorComponent
                | UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent
                | UiK8SAppsInstallCreateDisplayNameErrorComponent
                | UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent
                | UiK8SAppsInstallCreateHaEnabledErrorComponent
                | UiK8SAppsInstallCreateHelmChartErrorComponent
                | UiK8SAppsInstallCreateInstallationFailedErrorComponent
                | UiK8SAppsInstallCreateInstallationRunningErrorComponent
                | UiK8SAppsInstallCreateInstalledErrorComponent
                | UiK8SAppsInstallCreateInstalledVersionErrorComponent
                | UiK8SAppsInstallCreateK8SClusterErrorComponent
                | UiK8SAppsInstallCreateKindErrorComponent
                | UiK8SAppsInstallCreateLabelsErrorComponent
                | UiK8SAppsInstallCreateLastInstallationErrorComponent
                | UiK8SAppsInstallCreateLastMetricsCheckErrorComponent
                | UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent
                | UiK8SAppsInstallCreateManagedByContentTypeErrorComponent
                | UiK8SAppsInstallCreateManagedByObjectIdErrorComponent
                | UiK8SAppsInstallCreateModifiedByUserErrorComponent
                | UiK8SAppsInstallCreateNameErrorComponent
                | UiK8SAppsInstallCreateNamespaceErrorComponent
                | UiK8SAppsInstallCreateNonFieldErrorsErrorComponent
                | UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent
                | UiK8SAppsInstallCreatePlatformServiceErrorComponent
                | UiK8SAppsInstallCreatePodsAvailableErrorComponent
                | UiK8SAppsInstallCreatePodsDetailsErrorComponent
                | UiK8SAppsInstallCreatePodsReadyErrorComponent
                | UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent
                | UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent
                | UiK8SAppsInstallCreatePodsStatusHashErrorComponent
                | UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent
                | UiK8SAppsInstallCreatePodsTotalErrorComponent
                | UiK8SAppsInstallCreatePodsUnavailableErrorComponent
                | UiK8SAppsInstallCreateProviderErrorComponent
                | UiK8SAppsInstallCreateProviderIdErrorComponent
                | UiK8SAppsInstallCreateProviderReferenceErrorComponent
                | UiK8SAppsInstallCreateReconciliationEnabledErrorComponent
                | UiK8SAppsInstallCreateScopeErrorComponent
                | UiK8SAppsInstallCreateSlaAvailabilityErrorComponent
                | UiK8SAppsInstallCreateSlaTargetErrorComponent
                | UiK8SAppsInstallCreateSlaWindowDaysErrorComponent
                | UiK8SAppsInstallCreateSloAvailabilityErrorComponent
                | UiK8SAppsInstallCreateSloTargetErrorComponent
                | UiK8SAppsInstallCreateSloWindowDaysErrorComponent
                | UiK8SAppsInstallCreateSourceErrorComponent
                | UiK8SAppsInstallCreateTargetAvailabilityErrorComponent
                | UiK8SAppsInstallCreateUninstallationFailedErrorComponent
                | UiK8SAppsInstallCreateUninstallationRunningErrorComponent
                | UiK8SAppsInstallCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_0 = (
                        UiK8SAppsInstallCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_1 = (
                        UiK8SAppsInstallCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_2 = (
                        UiK8SAppsInstallCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_3 = (
                        UiK8SAppsInstallCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_4 = (
                        UiK8SAppsInstallCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_5 = (
                        UiK8SAppsInstallCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_6 = (
                        UiK8SAppsInstallCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_7 = (
                        UiK8SAppsInstallCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_8 = (
                        UiK8SAppsInstallCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_9 = (
                        UiK8SAppsInstallCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_10 = (
                        UiK8SAppsInstallCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_11 = (
                        UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_12 = (
                        UiK8SAppsInstallCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_13 = (
                        UiK8SAppsInstallCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_14 = (
                        UiK8SAppsInstallCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_15 = (
                        UiK8SAppsInstallCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_16 = (
                        UiK8SAppsInstallCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_17 = (
                        UiK8SAppsInstallCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_18 = (
                        UiK8SAppsInstallCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_19 = (
                        UiK8SAppsInstallCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_20 = (
                        UiK8SAppsInstallCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_21 = (
                        UiK8SAppsInstallCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_22 = (
                        UiK8SAppsInstallCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_23 = (
                        UiK8SAppsInstallCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_24 = (
                        UiK8SAppsInstallCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_25 = (
                        UiK8SAppsInstallCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_26 = (
                        UiK8SAppsInstallCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_27 = (
                        UiK8SAppsInstallCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_28 = (
                        UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_29 = (
                        UiK8SAppsInstallCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_30 = (
                        UiK8SAppsInstallCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_31 = (
                        UiK8SAppsInstallCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_32 = (
                        UiK8SAppsInstallCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_33 = (
                        UiK8SAppsInstallCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_34 = (
                        UiK8SAppsInstallCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_35 = (
                        UiK8SAppsInstallCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_36 = (
                        UiK8SAppsInstallCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_37 = (
                        UiK8SAppsInstallCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_38 = (
                        UiK8SAppsInstallCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_39 = (
                        UiK8SAppsInstallCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_40 = (
                        UiK8SAppsInstallCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_41 = (
                        UiK8SAppsInstallCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_42 = (
                        UiK8SAppsInstallCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_43 = (
                        UiK8SAppsInstallCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_44 = (
                        UiK8SAppsInstallCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_45 = (
                        UiK8SAppsInstallCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_46 = (
                        UiK8SAppsInstallCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_47 = (
                        UiK8SAppsInstallCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_48 = (
                        UiK8SAppsInstallCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_49 = (
                        UiK8SAppsInstallCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_50 = (
                        UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_51 = (
                        UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_52 = (
                        UiK8SAppsInstallCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_53 = (
                        UiK8SAppsInstallCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_54 = (
                        UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_55 = (
                        UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_56 = (
                        UiK8SAppsInstallCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_57 = (
                        UiK8SAppsInstallCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_58 = (
                        UiK8SAppsInstallCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_59 = (
                        UiK8SAppsInstallCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_60 = (
                        UiK8SAppsInstallCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_61 = (
                        UiK8SAppsInstallCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_62 = (
                        UiK8SAppsInstallCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_install_create_error_type_63 = (
                        UiK8SAppsInstallCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_install_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ui_k8_s_apps_install_create_error_type_64 = (
                    UiK8SAppsInstallCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_ui_k8_s_apps_install_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        ui_k8s_apps_install_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        ui_k8s_apps_install_create_validation_error.additional_properties = d
        return ui_k8s_apps_install_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
