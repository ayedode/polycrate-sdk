from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_uninstall_create_active_error_component import (
        ApiV1KubernetesAppsUninstallCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_actual_availability_error_component import (
        ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_annotations_error_component import (
        ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_archived_at_error_component import (
        ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_archived_by_error_component import (
        ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_archived_error_component import (
        ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_archived_reason_error_component import (
        ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_error_component import (
        ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_package_error_component import (
        ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_block_error_component import (
        ApiV1KubernetesAppsUninstallCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_byoa_error_component import (
        ApiV1KubernetesAppsUninstallCreateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_component_error_component import (
        ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_user_error_component import (
        ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_criticality_error_component import (
        ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_debug_mode_error_component import (
        ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_description_error_component import (
        ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_display_name_error_component import (
        ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_helm_chart_error_component import (
        ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_installation_failed_error_component import (
        ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_installation_running_error_component import (
        ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_installed_error_component import (
        ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_installed_version_error_component import (
        ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_kind_error_component import (
        ApiV1KubernetesAppsUninstallCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_labels_error_component import (
        ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_last_installation_error_component import (
        ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_name_error_component import (
        ApiV1KubernetesAppsUninstallCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_namespace_error_component import (
        ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_platform_service_error_component import (
        ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_available_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_details_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_ready_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_total_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_provider_error_component import (
        ApiV1KubernetesAppsUninstallCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_provider_id_error_component import (
        ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_provider_reference_error_component import (
        ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_scope_error_component import (
        ApiV1KubernetesAppsUninstallCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_sla_availability_error_component import (
        ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_sla_target_error_component import (
        ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_slo_availability_error_component import (
        ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_slo_target_error_component import (
        ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_source_error_component import (
        ApiV1KubernetesAppsUninstallCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_target_availability_error_component import (
        ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_uninstall_create_uninstalled_error_component import (
        ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsUninstallCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsUninstallCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsUninstallCreateActiveErrorComponent |
            ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent |
            ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsUninstallCreateBlockErrorComponent | ApiV1KubernetesAppsUninstallCreateByoaErrorComponent |
            ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent |
            ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent |
            ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent |
            ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent |
            ApiV1KubernetesAppsUninstallCreateKindErrorComponent | ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent |
            ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsUninstallCreateNameErrorComponent | ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent
            | ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsUninstallCreateProviderErrorComponent |
            ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent |
            ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsUninstallCreateScopeErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsUninstallCreateSourceErrorComponent |
            ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsUninstallCreateActiveErrorComponent
        | ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent
        | ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsUninstallCreateBlockErrorComponent
        | ApiV1KubernetesAppsUninstallCreateByoaErrorComponent
        | ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent
        | ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsUninstallCreateKindErrorComponent
        | ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent
        | ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsUninstallCreateNameErrorComponent
        | ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsUninstallCreateProviderErrorComponent
        | ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsUninstallCreateScopeErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsUninstallCreateSourceErrorComponent
        | ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_uninstall_create_active_error_component import (
            ApiV1KubernetesAppsUninstallCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_actual_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_annotations_error_component import (
            ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_at_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_by_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_reason_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_error_component import (
            ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_package_error_component import (
            ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_block_error_component import (
            ApiV1KubernetesAppsUninstallCreateBlockErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_byoa_error_component import (
            ApiV1KubernetesAppsUninstallCreateByoaErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_component_error_component import (
            ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_user_error_component import (
            ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_criticality_error_component import (
            ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_debug_mode_error_component import (
            ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_description_error_component import (
            ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_display_name_error_component import (
            ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_helm_chart_error_component import (
            ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installation_failed_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installation_running_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installed_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installed_version_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_kind_error_component import (
            ApiV1KubernetesAppsUninstallCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_labels_error_component import (
            ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_installation_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_name_error_component import (
            ApiV1KubernetesAppsUninstallCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_namespace_error_component import (
            ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_platform_service_error_component import (
            ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_available_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_details_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_ready_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_total_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_id_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_reference_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_scope_error_component import (
            ApiV1KubernetesAppsUninstallCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_target_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_target_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_source_error_component import (
            ApiV1KubernetesAppsUninstallCreateSourceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_target_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstalled_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_uninstall_create_active_error_component import (
            ApiV1KubernetesAppsUninstallCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_actual_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_annotations_error_component import (
            ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_at_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_by_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_archived_reason_error_component import (
            ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_error_component import (
            ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_artifact_package_error_component import (
            ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_block_error_component import (
            ApiV1KubernetesAppsUninstallCreateBlockErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_byoa_error_component import (
            ApiV1KubernetesAppsUninstallCreateByoaErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_component_error_component import (
            ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_created_by_user_error_component import (
            ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_criticality_error_component import (
            ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_debug_mode_error_component import (
            ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_description_error_component import (
            ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_display_name_error_component import (
            ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_helm_chart_error_component import (
            ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installation_failed_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installation_running_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installed_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_installed_version_error_component import (
            ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_kind_error_component import (
            ApiV1KubernetesAppsUninstallCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_labels_error_component import (
            ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_installation_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_name_error_component import (
            ApiV1KubernetesAppsUninstallCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_namespace_error_component import (
            ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_platform_service_error_component import (
            ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_available_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_details_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_ready_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_total_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_id_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_provider_reference_error_component import (
            ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_scope_error_component import (
            ApiV1KubernetesAppsUninstallCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_target_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_target_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_source_error_component import (
            ApiV1KubernetesAppsUninstallCreateSourceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_target_availability_error_component import (
            ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_uninstall_create_uninstalled_error_component import (
            ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsUninstallCreateActiveErrorComponent
                | ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent
                | ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsUninstallCreateBlockErrorComponent
                | ApiV1KubernetesAppsUninstallCreateByoaErrorComponent
                | ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent
                | ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsUninstallCreateKindErrorComponent
                | ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent
                | ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsUninstallCreateNameErrorComponent
                | ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsUninstallCreateProviderErrorComponent
                | ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsUninstallCreateScopeErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsUninstallCreateSourceErrorComponent
                | ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_0 = (
                        ApiV1KubernetesAppsUninstallCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_1 = (
                        ApiV1KubernetesAppsUninstallCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_2 = (
                        ApiV1KubernetesAppsUninstallCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_3 = (
                        ApiV1KubernetesAppsUninstallCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_4 = (
                        ApiV1KubernetesAppsUninstallCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_5 = (
                        ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_6 = (
                        ApiV1KubernetesAppsUninstallCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_7 = (
                        ApiV1KubernetesAppsUninstallCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_8 = (
                        ApiV1KubernetesAppsUninstallCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_9 = (
                        ApiV1KubernetesAppsUninstallCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_10 = (
                        ApiV1KubernetesAppsUninstallCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_11 = (
                        ApiV1KubernetesAppsUninstallCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_12 = (
                        ApiV1KubernetesAppsUninstallCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_13 = (
                        ApiV1KubernetesAppsUninstallCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_14 = (
                        ApiV1KubernetesAppsUninstallCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_15 = (
                        ApiV1KubernetesAppsUninstallCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_16 = (
                        ApiV1KubernetesAppsUninstallCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_17 = (
                        ApiV1KubernetesAppsUninstallCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_18 = (
                        ApiV1KubernetesAppsUninstallCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_19 = (
                        ApiV1KubernetesAppsUninstallCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_20 = (
                        ApiV1KubernetesAppsUninstallCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_21 = (
                        ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_22 = (
                        ApiV1KubernetesAppsUninstallCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_23 = (
                        ApiV1KubernetesAppsUninstallCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_24 = (
                        ApiV1KubernetesAppsUninstallCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_25 = (
                        ApiV1KubernetesAppsUninstallCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_26 = (
                        ApiV1KubernetesAppsUninstallCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_27 = (
                        ApiV1KubernetesAppsUninstallCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_28 = (
                        ApiV1KubernetesAppsUninstallCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_29 = (
                        ApiV1KubernetesAppsUninstallCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_30 = (
                        ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_31 = (
                        ApiV1KubernetesAppsUninstallCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_32 = (
                        ApiV1KubernetesAppsUninstallCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_33 = (
                        ApiV1KubernetesAppsUninstallCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_34 = (
                        ApiV1KubernetesAppsUninstallCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_35 = (
                        ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_36 = (
                        ApiV1KubernetesAppsUninstallCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_37 = (
                        ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_38 = (
                        ApiV1KubernetesAppsUninstallCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_39 = (
                        ApiV1KubernetesAppsUninstallCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_40 = (
                        ApiV1KubernetesAppsUninstallCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_41 = (
                        ApiV1KubernetesAppsUninstallCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_42 = (
                        ApiV1KubernetesAppsUninstallCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_43 = (
                        ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_44 = (
                        ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_45 = (
                        ApiV1KubernetesAppsUninstallCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_46 = (
                        ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_47 = (
                        ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_48 = (
                        ApiV1KubernetesAppsUninstallCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_49 = (
                        ApiV1KubernetesAppsUninstallCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_50 = (
                        ApiV1KubernetesAppsUninstallCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_51 = (
                        ApiV1KubernetesAppsUninstallCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_52 = (
                        ApiV1KubernetesAppsUninstallCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_53 = (
                        ApiV1KubernetesAppsUninstallCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_54 = (
                        ApiV1KubernetesAppsUninstallCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_55 = (
                        ApiV1KubernetesAppsUninstallCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_56 = (
                        ApiV1KubernetesAppsUninstallCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_57 = (
                        ApiV1KubernetesAppsUninstallCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_58 = (
                        ApiV1KubernetesAppsUninstallCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_59 = (
                        ApiV1KubernetesAppsUninstallCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_60 = (
                        ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_61 = (
                        ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_62 = (
                        ApiV1KubernetesAppsUninstallCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_63 = (
                        ApiV1KubernetesAppsUninstallCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_64 = (
                    ApiV1KubernetesAppsUninstallCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_uninstall_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_uninstall_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_uninstall_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_uninstall_create_validation_error

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
