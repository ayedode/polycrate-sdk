from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.ui_k8s_apps_uninstall_create_active_error_component import (
        UiK8SAppsUninstallCreateActiveErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_actual_availability_error_component import (
        UiK8SAppsUninstallCreateActualAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_annotations_error_component import (
        UiK8SAppsUninstallCreateAnnotationsErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_archived_at_error_component import (
        UiK8SAppsUninstallCreateArchivedAtErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_archived_by_error_component import (
        UiK8SAppsUninstallCreateArchivedByErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_archived_error_component import (
        UiK8SAppsUninstallCreateArchivedErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_archived_reason_error_component import (
        UiK8SAppsUninstallCreateArchivedReasonErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_artifact_error_component import (
        UiK8SAppsUninstallCreateArtifactErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_artifact_package_error_component import (
        UiK8SAppsUninstallCreateArtifactPackageErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_block_error_component import UiK8SAppsUninstallCreateBlockErrorComponent
    from ..models.ui_k8s_apps_uninstall_create_byoa_error_component import UiK8SAppsUninstallCreateByoaErrorComponent
    from ..models.ui_k8s_apps_uninstall_create_catalogue_app_error_component import (
        UiK8SAppsUninstallCreateCatalogueAppErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_created_by_component_error_component import (
        UiK8SAppsUninstallCreateCreatedByComponentErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_created_by_user_error_component import (
        UiK8SAppsUninstallCreateCreatedByUserErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_criticality_error_component import (
        UiK8SAppsUninstallCreateCriticalityErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_debug_mode_error_component import (
        UiK8SAppsUninstallCreateDebugModeErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_description_error_component import (
        UiK8SAppsUninstallCreateDescriptionErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_discovery_enabled_error_component import (
        UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_display_name_error_component import (
        UiK8SAppsUninstallCreateDisplayNameErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_excluded_from_downtime_until_error_component import (
        UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_ha_enabled_error_component import (
        UiK8SAppsUninstallCreateHaEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_helm_chart_error_component import (
        UiK8SAppsUninstallCreateHelmChartErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_installation_failed_error_component import (
        UiK8SAppsUninstallCreateInstallationFailedErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_installation_running_error_component import (
        UiK8SAppsUninstallCreateInstallationRunningErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_installed_error_component import (
        UiK8SAppsUninstallCreateInstalledErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_installed_version_error_component import (
        UiK8SAppsUninstallCreateInstalledVersionErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_k8s_cluster_error_component import (
        UiK8SAppsUninstallCreateK8SClusterErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_kind_error_component import UiK8SAppsUninstallCreateKindErrorComponent
    from ..models.ui_k8s_apps_uninstall_create_labels_error_component import (
        UiK8SAppsUninstallCreateLabelsErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_last_installation_error_component import (
        UiK8SAppsUninstallCreateLastInstallationErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_last_metrics_check_error_component import (
        UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
        UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_managed_by_content_type_error_component import (
        UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_managed_by_object_id_error_component import (
        UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_modified_by_user_error_component import (
        UiK8SAppsUninstallCreateModifiedByUserErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_name_error_component import UiK8SAppsUninstallCreateNameErrorComponent
    from ..models.ui_k8s_apps_uninstall_create_namespace_error_component import (
        UiK8SAppsUninstallCreateNamespaceErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_non_field_errors_error_component import (
        UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_platform_dns_record_created_error_component import (
        UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_platform_service_error_component import (
        UiK8SAppsUninstallCreatePlatformServiceErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_available_error_component import (
        UiK8SAppsUninstallCreatePodsAvailableErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_details_error_component import (
        UiK8SAppsUninstallCreatePodsDetailsErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_ready_error_component import (
        UiK8SAppsUninstallCreatePodsReadyErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
        UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_total_error_component import (
        UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_status_hash_error_component import (
        UiK8SAppsUninstallCreatePodsStatusHashErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_status_updated_at_error_component import (
        UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_total_error_component import (
        UiK8SAppsUninstallCreatePodsTotalErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_pods_unavailable_error_component import (
        UiK8SAppsUninstallCreatePodsUnavailableErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_provider_error_component import (
        UiK8SAppsUninstallCreateProviderErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_provider_id_error_component import (
        UiK8SAppsUninstallCreateProviderIdErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_provider_reference_error_component import (
        UiK8SAppsUninstallCreateProviderReferenceErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_reconciliation_enabled_error_component import (
        UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_scope_error_component import UiK8SAppsUninstallCreateScopeErrorComponent
    from ..models.ui_k8s_apps_uninstall_create_sla_availability_error_component import (
        UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_sla_target_error_component import (
        UiK8SAppsUninstallCreateSlaTargetErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_sla_window_days_error_component import (
        UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_slo_availability_error_component import (
        UiK8SAppsUninstallCreateSloAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_slo_target_error_component import (
        UiK8SAppsUninstallCreateSloTargetErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_slo_window_days_error_component import (
        UiK8SAppsUninstallCreateSloWindowDaysErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_source_error_component import (
        UiK8SAppsUninstallCreateSourceErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_target_availability_error_component import (
        UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_uninstallation_failed_error_component import (
        UiK8SAppsUninstallCreateUninstallationFailedErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_uninstallation_running_error_component import (
        UiK8SAppsUninstallCreateUninstallationRunningErrorComponent,
    )
    from ..models.ui_k8s_apps_uninstall_create_uninstalled_error_component import (
        UiK8SAppsUninstallCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="UiK8SAppsUninstallCreateValidationError")


@_attrs_define
class UiK8SAppsUninstallCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[UiK8SAppsUninstallCreateActiveErrorComponent |
            UiK8SAppsUninstallCreateActualAvailabilityErrorComponent | UiK8SAppsUninstallCreateAnnotationsErrorComponent |
            UiK8SAppsUninstallCreateArchivedAtErrorComponent | UiK8SAppsUninstallCreateArchivedByErrorComponent |
            UiK8SAppsUninstallCreateArchivedErrorComponent | UiK8SAppsUninstallCreateArchivedReasonErrorComponent |
            UiK8SAppsUninstallCreateArtifactErrorComponent | UiK8SAppsUninstallCreateArtifactPackageErrorComponent |
            UiK8SAppsUninstallCreateBlockErrorComponent | UiK8SAppsUninstallCreateByoaErrorComponent |
            UiK8SAppsUninstallCreateCatalogueAppErrorComponent | UiK8SAppsUninstallCreateCreatedByComponentErrorComponent |
            UiK8SAppsUninstallCreateCreatedByUserErrorComponent | UiK8SAppsUninstallCreateCriticalityErrorComponent |
            UiK8SAppsUninstallCreateDebugModeErrorComponent | UiK8SAppsUninstallCreateDescriptionErrorComponent |
            UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent | UiK8SAppsUninstallCreateDisplayNameErrorComponent |
            UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent |
            UiK8SAppsUninstallCreateHaEnabledErrorComponent | UiK8SAppsUninstallCreateHelmChartErrorComponent |
            UiK8SAppsUninstallCreateInstallationFailedErrorComponent |
            UiK8SAppsUninstallCreateInstallationRunningErrorComponent | UiK8SAppsUninstallCreateInstalledErrorComponent |
            UiK8SAppsUninstallCreateInstalledVersionErrorComponent | UiK8SAppsUninstallCreateK8SClusterErrorComponent |
            UiK8SAppsUninstallCreateKindErrorComponent | UiK8SAppsUninstallCreateLabelsErrorComponent |
            UiK8SAppsUninstallCreateLastInstallationErrorComponent | UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent
            | UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent |
            UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent |
            UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent | UiK8SAppsUninstallCreateModifiedByUserErrorComponent |
            UiK8SAppsUninstallCreateNameErrorComponent | UiK8SAppsUninstallCreateNamespaceErrorComponent |
            UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent |
            UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent |
            UiK8SAppsUninstallCreatePlatformServiceErrorComponent | UiK8SAppsUninstallCreatePodsAvailableErrorComponent |
            UiK8SAppsUninstallCreatePodsDetailsErrorComponent | UiK8SAppsUninstallCreatePodsReadyErrorComponent |
            UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent |
            UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent |
            UiK8SAppsUninstallCreatePodsStatusHashErrorComponent | UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent
            | UiK8SAppsUninstallCreatePodsTotalErrorComponent | UiK8SAppsUninstallCreatePodsUnavailableErrorComponent |
            UiK8SAppsUninstallCreateProviderErrorComponent | UiK8SAppsUninstallCreateProviderIdErrorComponent |
            UiK8SAppsUninstallCreateProviderReferenceErrorComponent |
            UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent | UiK8SAppsUninstallCreateScopeErrorComponent |
            UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent | UiK8SAppsUninstallCreateSlaTargetErrorComponent |
            UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent | UiK8SAppsUninstallCreateSloAvailabilityErrorComponent |
            UiK8SAppsUninstallCreateSloTargetErrorComponent | UiK8SAppsUninstallCreateSloWindowDaysErrorComponent |
            UiK8SAppsUninstallCreateSourceErrorComponent | UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent |
            UiK8SAppsUninstallCreateUninstallationFailedErrorComponent |
            UiK8SAppsUninstallCreateUninstallationRunningErrorComponent |
            UiK8SAppsUninstallCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        UiK8SAppsUninstallCreateActiveErrorComponent
        | UiK8SAppsUninstallCreateActualAvailabilityErrorComponent
        | UiK8SAppsUninstallCreateAnnotationsErrorComponent
        | UiK8SAppsUninstallCreateArchivedAtErrorComponent
        | UiK8SAppsUninstallCreateArchivedByErrorComponent
        | UiK8SAppsUninstallCreateArchivedErrorComponent
        | UiK8SAppsUninstallCreateArchivedReasonErrorComponent
        | UiK8SAppsUninstallCreateArtifactErrorComponent
        | UiK8SAppsUninstallCreateArtifactPackageErrorComponent
        | UiK8SAppsUninstallCreateBlockErrorComponent
        | UiK8SAppsUninstallCreateByoaErrorComponent
        | UiK8SAppsUninstallCreateCatalogueAppErrorComponent
        | UiK8SAppsUninstallCreateCreatedByComponentErrorComponent
        | UiK8SAppsUninstallCreateCreatedByUserErrorComponent
        | UiK8SAppsUninstallCreateCriticalityErrorComponent
        | UiK8SAppsUninstallCreateDebugModeErrorComponent
        | UiK8SAppsUninstallCreateDescriptionErrorComponent
        | UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent
        | UiK8SAppsUninstallCreateDisplayNameErrorComponent
        | UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent
        | UiK8SAppsUninstallCreateHaEnabledErrorComponent
        | UiK8SAppsUninstallCreateHelmChartErrorComponent
        | UiK8SAppsUninstallCreateInstallationFailedErrorComponent
        | UiK8SAppsUninstallCreateInstallationRunningErrorComponent
        | UiK8SAppsUninstallCreateInstalledErrorComponent
        | UiK8SAppsUninstallCreateInstalledVersionErrorComponent
        | UiK8SAppsUninstallCreateK8SClusterErrorComponent
        | UiK8SAppsUninstallCreateKindErrorComponent
        | UiK8SAppsUninstallCreateLabelsErrorComponent
        | UiK8SAppsUninstallCreateLastInstallationErrorComponent
        | UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent
        | UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent
        | UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent
        | UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent
        | UiK8SAppsUninstallCreateModifiedByUserErrorComponent
        | UiK8SAppsUninstallCreateNameErrorComponent
        | UiK8SAppsUninstallCreateNamespaceErrorComponent
        | UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent
        | UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent
        | UiK8SAppsUninstallCreatePlatformServiceErrorComponent
        | UiK8SAppsUninstallCreatePodsAvailableErrorComponent
        | UiK8SAppsUninstallCreatePodsDetailsErrorComponent
        | UiK8SAppsUninstallCreatePodsReadyErrorComponent
        | UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent
        | UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent
        | UiK8SAppsUninstallCreatePodsStatusHashErrorComponent
        | UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent
        | UiK8SAppsUninstallCreatePodsTotalErrorComponent
        | UiK8SAppsUninstallCreatePodsUnavailableErrorComponent
        | UiK8SAppsUninstallCreateProviderErrorComponent
        | UiK8SAppsUninstallCreateProviderIdErrorComponent
        | UiK8SAppsUninstallCreateProviderReferenceErrorComponent
        | UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent
        | UiK8SAppsUninstallCreateScopeErrorComponent
        | UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent
        | UiK8SAppsUninstallCreateSlaTargetErrorComponent
        | UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent
        | UiK8SAppsUninstallCreateSloAvailabilityErrorComponent
        | UiK8SAppsUninstallCreateSloTargetErrorComponent
        | UiK8SAppsUninstallCreateSloWindowDaysErrorComponent
        | UiK8SAppsUninstallCreateSourceErrorComponent
        | UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent
        | UiK8SAppsUninstallCreateUninstallationFailedErrorComponent
        | UiK8SAppsUninstallCreateUninstallationRunningErrorComponent
        | UiK8SAppsUninstallCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_k8s_apps_uninstall_create_active_error_component import (
            UiK8SAppsUninstallCreateActiveErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_actual_availability_error_component import (
            UiK8SAppsUninstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_annotations_error_component import (
            UiK8SAppsUninstallCreateAnnotationsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_at_error_component import (
            UiK8SAppsUninstallCreateArchivedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_by_error_component import (
            UiK8SAppsUninstallCreateArchivedByErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_error_component import (
            UiK8SAppsUninstallCreateArchivedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_reason_error_component import (
            UiK8SAppsUninstallCreateArchivedReasonErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_artifact_error_component import (
            UiK8SAppsUninstallCreateArtifactErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_artifact_package_error_component import (
            UiK8SAppsUninstallCreateArtifactPackageErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_block_error_component import (
            UiK8SAppsUninstallCreateBlockErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_byoa_error_component import (
            UiK8SAppsUninstallCreateByoaErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_catalogue_app_error_component import (
            UiK8SAppsUninstallCreateCatalogueAppErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_created_by_component_error_component import (
            UiK8SAppsUninstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_created_by_user_error_component import (
            UiK8SAppsUninstallCreateCreatedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_criticality_error_component import (
            UiK8SAppsUninstallCreateCriticalityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_debug_mode_error_component import (
            UiK8SAppsUninstallCreateDebugModeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_description_error_component import (
            UiK8SAppsUninstallCreateDescriptionErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_discovery_enabled_error_component import (
            UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_display_name_error_component import (
            UiK8SAppsUninstallCreateDisplayNameErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_excluded_from_downtime_until_error_component import (
            UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_ha_enabled_error_component import (
            UiK8SAppsUninstallCreateHaEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_helm_chart_error_component import (
            UiK8SAppsUninstallCreateHelmChartErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installation_failed_error_component import (
            UiK8SAppsUninstallCreateInstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installation_running_error_component import (
            UiK8SAppsUninstallCreateInstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installed_error_component import (
            UiK8SAppsUninstallCreateInstalledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installed_version_error_component import (
            UiK8SAppsUninstallCreateInstalledVersionErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_kind_error_component import (
            UiK8SAppsUninstallCreateKindErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_labels_error_component import (
            UiK8SAppsUninstallCreateLabelsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_installation_error_component import (
            UiK8SAppsUninstallCreateLastInstallationErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_metrics_check_error_component import (
            UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
            UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_managed_by_content_type_error_component import (
            UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_managed_by_object_id_error_component import (
            UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_modified_by_user_error_component import (
            UiK8SAppsUninstallCreateModifiedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_name_error_component import (
            UiK8SAppsUninstallCreateNameErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_namespace_error_component import (
            UiK8SAppsUninstallCreateNamespaceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_non_field_errors_error_component import (
            UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_platform_dns_record_created_error_component import (
            UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_platform_service_error_component import (
            UiK8SAppsUninstallCreatePlatformServiceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_available_error_component import (
            UiK8SAppsUninstallCreatePodsAvailableErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_details_error_component import (
            UiK8SAppsUninstallCreatePodsDetailsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_ready_error_component import (
            UiK8SAppsUninstallCreatePodsReadyErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
            UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_total_error_component import (
            UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_status_hash_error_component import (
            UiK8SAppsUninstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_status_updated_at_error_component import (
            UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_total_error_component import (
            UiK8SAppsUninstallCreatePodsTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_unavailable_error_component import (
            UiK8SAppsUninstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_error_component import (
            UiK8SAppsUninstallCreateProviderErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_id_error_component import (
            UiK8SAppsUninstallCreateProviderIdErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_reference_error_component import (
            UiK8SAppsUninstallCreateProviderReferenceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_reconciliation_enabled_error_component import (
            UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_scope_error_component import (
            UiK8SAppsUninstallCreateScopeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_availability_error_component import (
            UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_target_error_component import (
            UiK8SAppsUninstallCreateSlaTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_window_days_error_component import (
            UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_availability_error_component import (
            UiK8SAppsUninstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_target_error_component import (
            UiK8SAppsUninstallCreateSloTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_window_days_error_component import (
            UiK8SAppsUninstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_source_error_component import (
            UiK8SAppsUninstallCreateSourceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_target_availability_error_component import (
            UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstallation_failed_error_component import (
            UiK8SAppsUninstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstallation_running_error_component import (
            UiK8SAppsUninstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstalled_error_component import (
            UiK8SAppsUninstallCreateUninstalledErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, UiK8SAppsUninstallCreateCatalogueAppErrorComponent):
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
        from ..models.ui_k8s_apps_uninstall_create_active_error_component import (
            UiK8SAppsUninstallCreateActiveErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_actual_availability_error_component import (
            UiK8SAppsUninstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_annotations_error_component import (
            UiK8SAppsUninstallCreateAnnotationsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_at_error_component import (
            UiK8SAppsUninstallCreateArchivedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_by_error_component import (
            UiK8SAppsUninstallCreateArchivedByErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_error_component import (
            UiK8SAppsUninstallCreateArchivedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_archived_reason_error_component import (
            UiK8SAppsUninstallCreateArchivedReasonErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_artifact_error_component import (
            UiK8SAppsUninstallCreateArtifactErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_artifact_package_error_component import (
            UiK8SAppsUninstallCreateArtifactPackageErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_block_error_component import (
            UiK8SAppsUninstallCreateBlockErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_byoa_error_component import (
            UiK8SAppsUninstallCreateByoaErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_catalogue_app_error_component import (
            UiK8SAppsUninstallCreateCatalogueAppErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_created_by_component_error_component import (
            UiK8SAppsUninstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_created_by_user_error_component import (
            UiK8SAppsUninstallCreateCreatedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_criticality_error_component import (
            UiK8SAppsUninstallCreateCriticalityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_debug_mode_error_component import (
            UiK8SAppsUninstallCreateDebugModeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_description_error_component import (
            UiK8SAppsUninstallCreateDescriptionErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_discovery_enabled_error_component import (
            UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_display_name_error_component import (
            UiK8SAppsUninstallCreateDisplayNameErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_excluded_from_downtime_until_error_component import (
            UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_ha_enabled_error_component import (
            UiK8SAppsUninstallCreateHaEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_helm_chart_error_component import (
            UiK8SAppsUninstallCreateHelmChartErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installation_failed_error_component import (
            UiK8SAppsUninstallCreateInstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installation_running_error_component import (
            UiK8SAppsUninstallCreateInstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installed_error_component import (
            UiK8SAppsUninstallCreateInstalledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_installed_version_error_component import (
            UiK8SAppsUninstallCreateInstalledVersionErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_k8s_cluster_error_component import (
            UiK8SAppsUninstallCreateK8SClusterErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_kind_error_component import (
            UiK8SAppsUninstallCreateKindErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_labels_error_component import (
            UiK8SAppsUninstallCreateLabelsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_installation_error_component import (
            UiK8SAppsUninstallCreateLastInstallationErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_metrics_check_error_component import (
            UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
            UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_managed_by_content_type_error_component import (
            UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_managed_by_object_id_error_component import (
            UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_modified_by_user_error_component import (
            UiK8SAppsUninstallCreateModifiedByUserErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_name_error_component import (
            UiK8SAppsUninstallCreateNameErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_namespace_error_component import (
            UiK8SAppsUninstallCreateNamespaceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_non_field_errors_error_component import (
            UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_platform_dns_record_created_error_component import (
            UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_platform_service_error_component import (
            UiK8SAppsUninstallCreatePlatformServiceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_available_error_component import (
            UiK8SAppsUninstallCreatePodsAvailableErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_details_error_component import (
            UiK8SAppsUninstallCreatePodsDetailsErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_ready_error_component import (
            UiK8SAppsUninstallCreatePodsReadyErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
            UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_restart_count_total_error_component import (
            UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_status_hash_error_component import (
            UiK8SAppsUninstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_status_updated_at_error_component import (
            UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_total_error_component import (
            UiK8SAppsUninstallCreatePodsTotalErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_pods_unavailable_error_component import (
            UiK8SAppsUninstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_error_component import (
            UiK8SAppsUninstallCreateProviderErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_id_error_component import (
            UiK8SAppsUninstallCreateProviderIdErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_provider_reference_error_component import (
            UiK8SAppsUninstallCreateProviderReferenceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_reconciliation_enabled_error_component import (
            UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_scope_error_component import (
            UiK8SAppsUninstallCreateScopeErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_availability_error_component import (
            UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_target_error_component import (
            UiK8SAppsUninstallCreateSlaTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_sla_window_days_error_component import (
            UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_availability_error_component import (
            UiK8SAppsUninstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_target_error_component import (
            UiK8SAppsUninstallCreateSloTargetErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_slo_window_days_error_component import (
            UiK8SAppsUninstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_source_error_component import (
            UiK8SAppsUninstallCreateSourceErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_target_availability_error_component import (
            UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstallation_failed_error_component import (
            UiK8SAppsUninstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstallation_running_error_component import (
            UiK8SAppsUninstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.ui_k8s_apps_uninstall_create_uninstalled_error_component import (
            UiK8SAppsUninstallCreateUninstalledErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                UiK8SAppsUninstallCreateActiveErrorComponent
                | UiK8SAppsUninstallCreateActualAvailabilityErrorComponent
                | UiK8SAppsUninstallCreateAnnotationsErrorComponent
                | UiK8SAppsUninstallCreateArchivedAtErrorComponent
                | UiK8SAppsUninstallCreateArchivedByErrorComponent
                | UiK8SAppsUninstallCreateArchivedErrorComponent
                | UiK8SAppsUninstallCreateArchivedReasonErrorComponent
                | UiK8SAppsUninstallCreateArtifactErrorComponent
                | UiK8SAppsUninstallCreateArtifactPackageErrorComponent
                | UiK8SAppsUninstallCreateBlockErrorComponent
                | UiK8SAppsUninstallCreateByoaErrorComponent
                | UiK8SAppsUninstallCreateCatalogueAppErrorComponent
                | UiK8SAppsUninstallCreateCreatedByComponentErrorComponent
                | UiK8SAppsUninstallCreateCreatedByUserErrorComponent
                | UiK8SAppsUninstallCreateCriticalityErrorComponent
                | UiK8SAppsUninstallCreateDebugModeErrorComponent
                | UiK8SAppsUninstallCreateDescriptionErrorComponent
                | UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent
                | UiK8SAppsUninstallCreateDisplayNameErrorComponent
                | UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent
                | UiK8SAppsUninstallCreateHaEnabledErrorComponent
                | UiK8SAppsUninstallCreateHelmChartErrorComponent
                | UiK8SAppsUninstallCreateInstallationFailedErrorComponent
                | UiK8SAppsUninstallCreateInstallationRunningErrorComponent
                | UiK8SAppsUninstallCreateInstalledErrorComponent
                | UiK8SAppsUninstallCreateInstalledVersionErrorComponent
                | UiK8SAppsUninstallCreateK8SClusterErrorComponent
                | UiK8SAppsUninstallCreateKindErrorComponent
                | UiK8SAppsUninstallCreateLabelsErrorComponent
                | UiK8SAppsUninstallCreateLastInstallationErrorComponent
                | UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent
                | UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent
                | UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent
                | UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent
                | UiK8SAppsUninstallCreateModifiedByUserErrorComponent
                | UiK8SAppsUninstallCreateNameErrorComponent
                | UiK8SAppsUninstallCreateNamespaceErrorComponent
                | UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent
                | UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent
                | UiK8SAppsUninstallCreatePlatformServiceErrorComponent
                | UiK8SAppsUninstallCreatePodsAvailableErrorComponent
                | UiK8SAppsUninstallCreatePodsDetailsErrorComponent
                | UiK8SAppsUninstallCreatePodsReadyErrorComponent
                | UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent
                | UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent
                | UiK8SAppsUninstallCreatePodsStatusHashErrorComponent
                | UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent
                | UiK8SAppsUninstallCreatePodsTotalErrorComponent
                | UiK8SAppsUninstallCreatePodsUnavailableErrorComponent
                | UiK8SAppsUninstallCreateProviderErrorComponent
                | UiK8SAppsUninstallCreateProviderIdErrorComponent
                | UiK8SAppsUninstallCreateProviderReferenceErrorComponent
                | UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent
                | UiK8SAppsUninstallCreateScopeErrorComponent
                | UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent
                | UiK8SAppsUninstallCreateSlaTargetErrorComponent
                | UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent
                | UiK8SAppsUninstallCreateSloAvailabilityErrorComponent
                | UiK8SAppsUninstallCreateSloTargetErrorComponent
                | UiK8SAppsUninstallCreateSloWindowDaysErrorComponent
                | UiK8SAppsUninstallCreateSourceErrorComponent
                | UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent
                | UiK8SAppsUninstallCreateUninstallationFailedErrorComponent
                | UiK8SAppsUninstallCreateUninstallationRunningErrorComponent
                | UiK8SAppsUninstallCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_0 = (
                        UiK8SAppsUninstallCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_1 = (
                        UiK8SAppsUninstallCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_2 = (
                        UiK8SAppsUninstallCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_3 = (
                        UiK8SAppsUninstallCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_4 = (
                        UiK8SAppsUninstallCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_5 = (
                        UiK8SAppsUninstallCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_6 = (
                        UiK8SAppsUninstallCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_7 = (
                        UiK8SAppsUninstallCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_8 = (
                        UiK8SAppsUninstallCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_9 = (
                        UiK8SAppsUninstallCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_10 = (
                        UiK8SAppsUninstallCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_11 = (
                        UiK8SAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_12 = (
                        UiK8SAppsUninstallCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_13 = (
                        UiK8SAppsUninstallCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_14 = (
                        UiK8SAppsUninstallCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_15 = (
                        UiK8SAppsUninstallCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_16 = (
                        UiK8SAppsUninstallCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_17 = (
                        UiK8SAppsUninstallCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_18 = (
                        UiK8SAppsUninstallCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_19 = (
                        UiK8SAppsUninstallCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_20 = (
                        UiK8SAppsUninstallCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_21 = (
                        UiK8SAppsUninstallCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_22 = (
                        UiK8SAppsUninstallCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_23 = (
                        UiK8SAppsUninstallCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_24 = (
                        UiK8SAppsUninstallCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_25 = (
                        UiK8SAppsUninstallCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_26 = (
                        UiK8SAppsUninstallCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_27 = (
                        UiK8SAppsUninstallCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_28 = (
                        UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_29 = (
                        UiK8SAppsUninstallCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_30 = (
                        UiK8SAppsUninstallCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_31 = (
                        UiK8SAppsUninstallCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_32 = (
                        UiK8SAppsUninstallCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_33 = (
                        UiK8SAppsUninstallCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_34 = (
                        UiK8SAppsUninstallCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_35 = (
                        UiK8SAppsUninstallCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_36 = (
                        UiK8SAppsUninstallCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_37 = (
                        UiK8SAppsUninstallCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_38 = (
                        UiK8SAppsUninstallCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_39 = (
                        UiK8SAppsUninstallCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_40 = (
                        UiK8SAppsUninstallCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_41 = (
                        UiK8SAppsUninstallCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_42 = (
                        UiK8SAppsUninstallCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_43 = (
                        UiK8SAppsUninstallCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_44 = (
                        UiK8SAppsUninstallCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_45 = (
                        UiK8SAppsUninstallCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_46 = (
                        UiK8SAppsUninstallCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_47 = (
                        UiK8SAppsUninstallCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_48 = (
                        UiK8SAppsUninstallCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_49 = (
                        UiK8SAppsUninstallCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_50 = (
                        UiK8SAppsUninstallCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_51 = (
                        UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_52 = (
                        UiK8SAppsUninstallCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_53 = (
                        UiK8SAppsUninstallCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_54 = (
                        UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_55 = (
                        UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_56 = (
                        UiK8SAppsUninstallCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_57 = (
                        UiK8SAppsUninstallCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_58 = (
                        UiK8SAppsUninstallCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_59 = (
                        UiK8SAppsUninstallCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_60 = (
                        UiK8SAppsUninstallCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_61 = (
                        UiK8SAppsUninstallCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_62 = (
                        UiK8SAppsUninstallCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ui_k8_s_apps_uninstall_create_error_type_63 = (
                        UiK8SAppsUninstallCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ui_k8_s_apps_uninstall_create_error_type_64 = (
                    UiK8SAppsUninstallCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_ui_k8_s_apps_uninstall_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        ui_k8s_apps_uninstall_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        ui_k8s_apps_uninstall_create_validation_error.additional_properties = d
        return ui_k8s_apps_uninstall_create_validation_error

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
