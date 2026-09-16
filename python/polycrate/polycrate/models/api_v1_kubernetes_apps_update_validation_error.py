from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_update_active_error_component import (
        ApiV1KubernetesAppsUpdateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_actual_availability_error_component import (
        ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_annotations_error_component import (
        ApiV1KubernetesAppsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_archived_at_error_component import (
        ApiV1KubernetesAppsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_archived_by_error_component import (
        ApiV1KubernetesAppsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_archived_error_component import (
        ApiV1KubernetesAppsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_archived_reason_error_component import (
        ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_artifact_error_component import (
        ApiV1KubernetesAppsUpdateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_artifact_package_error_component import (
        ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_block_error_component import (
        ApiV1KubernetesAppsUpdateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_byoa_error_component import ApiV1KubernetesAppsUpdateByoaErrorComponent
    from ..models.api_v1_kubernetes_apps_update_catalogue_app_error_component import (
        ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_created_by_component_error_component import (
        ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_created_by_user_error_component import (
        ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_criticality_error_component import (
        ApiV1KubernetesAppsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_debug_mode_error_component import (
        ApiV1KubernetesAppsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_description_error_component import (
        ApiV1KubernetesAppsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_discovery_enabled_error_component import (
        ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_display_name_error_component import (
        ApiV1KubernetesAppsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_ha_enabled_error_component import (
        ApiV1KubernetesAppsUpdateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_helm_chart_error_component import (
        ApiV1KubernetesAppsUpdateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_installation_failed_error_component import (
        ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_installation_running_error_component import (
        ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_installed_error_component import (
        ApiV1KubernetesAppsUpdateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_installed_version_error_component import (
        ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_k8s_cluster_error_component import (
        ApiV1KubernetesAppsUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_kind_error_component import ApiV1KubernetesAppsUpdateKindErrorComponent
    from ..models.api_v1_kubernetes_apps_update_labels_error_component import (
        ApiV1KubernetesAppsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_last_installation_error_component import (
        ApiV1KubernetesAppsUpdateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_last_metrics_check_error_component import (
        ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_modified_by_user_error_component import (
        ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_name_error_component import ApiV1KubernetesAppsUpdateNameErrorComponent
    from ..models.api_v1_kubernetes_apps_update_namespace_error_component import (
        ApiV1KubernetesAppsUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_non_field_errors_error_component import (
        ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_platform_service_error_component import (
        ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_available_error_component import (
        ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_details_error_component import (
        ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_ready_error_component import (
        ApiV1KubernetesAppsUpdatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_status_hash_error_component import (
        ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_total_error_component import (
        ApiV1KubernetesAppsUpdatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_pods_unavailable_error_component import (
        ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_provider_error_component import (
        ApiV1KubernetesAppsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_provider_id_error_component import (
        ApiV1KubernetesAppsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_provider_reference_error_component import (
        ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_scope_error_component import (
        ApiV1KubernetesAppsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_sla_availability_error_component import (
        ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_sla_target_error_component import (
        ApiV1KubernetesAppsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_sla_window_days_error_component import (
        ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_slo_availability_error_component import (
        ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_slo_target_error_component import (
        ApiV1KubernetesAppsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_slo_window_days_error_component import (
        ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_source_error_component import (
        ApiV1KubernetesAppsUpdateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_target_availability_error_component import (
        ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_uninstallation_running_error_component import (
        ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_update_uninstalled_error_component import (
        ApiV1KubernetesAppsUpdateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAppsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsUpdateActiveErrorComponent |
            ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent | ApiV1KubernetesAppsUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAppsUpdateArchivedAtErrorComponent | ApiV1KubernetesAppsUpdateArchivedByErrorComponent |
            ApiV1KubernetesAppsUpdateArchivedErrorComponent | ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsUpdateArtifactErrorComponent | ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsUpdateBlockErrorComponent | ApiV1KubernetesAppsUpdateByoaErrorComponent |
            ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent | ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent
            | ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent | ApiV1KubernetesAppsUpdateCriticalityErrorComponent |
            ApiV1KubernetesAppsUpdateDebugModeErrorComponent | ApiV1KubernetesAppsUpdateDescriptionErrorComponent |
            ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent | ApiV1KubernetesAppsUpdateDisplayNameErrorComponent |
            ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsUpdateHaEnabledErrorComponent | ApiV1KubernetesAppsUpdateHelmChartErrorComponent |
            ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent | ApiV1KubernetesAppsUpdateInstalledErrorComponent |
            ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent | ApiV1KubernetesAppsUpdateK8SClusterErrorComponent |
            ApiV1KubernetesAppsUpdateKindErrorComponent | ApiV1KubernetesAppsUpdateLabelsErrorComponent |
            ApiV1KubernetesAppsUpdateLastInstallationErrorComponent |
            ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent | ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent
            | ApiV1KubernetesAppsUpdateNameErrorComponent | ApiV1KubernetesAppsUpdateNamespaceErrorComponent |
            ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent | ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent | ApiV1KubernetesAppsUpdatePodsReadyErrorComponent |
            ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent | ApiV1KubernetesAppsUpdatePodsTotalErrorComponent |
            ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent | ApiV1KubernetesAppsUpdateProviderErrorComponent |
            ApiV1KubernetesAppsUpdateProviderIdErrorComponent | ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent | ApiV1KubernetesAppsUpdateScopeErrorComponent |
            ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent | ApiV1KubernetesAppsUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent | ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsUpdateSloTargetErrorComponent | ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsUpdateSourceErrorComponent | ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsUpdateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsUpdateActiveErrorComponent
        | ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAppsUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAppsUpdateArchivedByErrorComponent
        | ApiV1KubernetesAppsUpdateArchivedErrorComponent
        | ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsUpdateArtifactErrorComponent
        | ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsUpdateBlockErrorComponent
        | ApiV1KubernetesAppsUpdateByoaErrorComponent
        | ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsUpdateCriticalityErrorComponent
        | ApiV1KubernetesAppsUpdateDebugModeErrorComponent
        | ApiV1KubernetesAppsUpdateDescriptionErrorComponent
        | ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsUpdateHaEnabledErrorComponent
        | ApiV1KubernetesAppsUpdateHelmChartErrorComponent
        | ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsUpdateInstalledErrorComponent
        | ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsUpdateK8SClusterErrorComponent
        | ApiV1KubernetesAppsUpdateKindErrorComponent
        | ApiV1KubernetesAppsUpdateLabelsErrorComponent
        | ApiV1KubernetesAppsUpdateLastInstallationErrorComponent
        | ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsUpdateNameErrorComponent
        | ApiV1KubernetesAppsUpdateNamespaceErrorComponent
        | ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsUpdatePodsReadyErrorComponent
        | ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsUpdatePodsTotalErrorComponent
        | ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsUpdateProviderErrorComponent
        | ApiV1KubernetesAppsUpdateProviderIdErrorComponent
        | ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsUpdateScopeErrorComponent
        | ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsUpdateSloTargetErrorComponent
        | ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsUpdateSourceErrorComponent
        | ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsUpdateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_update_active_error_component import (
            ApiV1KubernetesAppsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_actual_availability_error_component import (
            ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_annotations_error_component import (
            ApiV1KubernetesAppsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_at_error_component import (
            ApiV1KubernetesAppsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_by_error_component import (
            ApiV1KubernetesAppsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_error_component import (
            ApiV1KubernetesAppsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_reason_error_component import (
            ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_artifact_error_component import (
            ApiV1KubernetesAppsUpdateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_artifact_package_error_component import (
            ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_block_error_component import (
            ApiV1KubernetesAppsUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_byoa_error_component import (
            ApiV1KubernetesAppsUpdateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_catalogue_app_error_component import (
            ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_created_by_component_error_component import (
            ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_created_by_user_error_component import (
            ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_criticality_error_component import (
            ApiV1KubernetesAppsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_debug_mode_error_component import (
            ApiV1KubernetesAppsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_description_error_component import (
            ApiV1KubernetesAppsUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_discovery_enabled_error_component import (
            ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_display_name_error_component import (
            ApiV1KubernetesAppsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_ha_enabled_error_component import (
            ApiV1KubernetesAppsUpdateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_helm_chart_error_component import (
            ApiV1KubernetesAppsUpdateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installation_failed_error_component import (
            ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installation_running_error_component import (
            ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installed_error_component import (
            ApiV1KubernetesAppsUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installed_version_error_component import (
            ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_kind_error_component import (
            ApiV1KubernetesAppsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_labels_error_component import (
            ApiV1KubernetesAppsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_installation_error_component import (
            ApiV1KubernetesAppsUpdateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_metrics_check_error_component import (
            ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_modified_by_user_error_component import (
            ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_name_error_component import (
            ApiV1KubernetesAppsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_namespace_error_component import (
            ApiV1KubernetesAppsUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_non_field_errors_error_component import (
            ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_platform_service_error_component import (
            ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_available_error_component import (
            ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_details_error_component import (
            ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_ready_error_component import (
            ApiV1KubernetesAppsUpdatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_status_hash_error_component import (
            ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_total_error_component import (
            ApiV1KubernetesAppsUpdatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_unavailable_error_component import (
            ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_error_component import (
            ApiV1KubernetesAppsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_id_error_component import (
            ApiV1KubernetesAppsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_reference_error_component import (
            ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_scope_error_component import (
            ApiV1KubernetesAppsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_availability_error_component import (
            ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_target_error_component import (
            ApiV1KubernetesAppsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_window_days_error_component import (
            ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_availability_error_component import (
            ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_target_error_component import (
            ApiV1KubernetesAppsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_window_days_error_component import (
            ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_source_error_component import (
            ApiV1KubernetesAppsUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_target_availability_error_component import (
            ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstallation_running_error_component import (
            ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstalled_error_component import (
            ApiV1KubernetesAppsUpdateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_update_active_error_component import (
            ApiV1KubernetesAppsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_actual_availability_error_component import (
            ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_annotations_error_component import (
            ApiV1KubernetesAppsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_at_error_component import (
            ApiV1KubernetesAppsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_by_error_component import (
            ApiV1KubernetesAppsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_error_component import (
            ApiV1KubernetesAppsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_archived_reason_error_component import (
            ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_artifact_error_component import (
            ApiV1KubernetesAppsUpdateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_artifact_package_error_component import (
            ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_block_error_component import (
            ApiV1KubernetesAppsUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_byoa_error_component import (
            ApiV1KubernetesAppsUpdateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_catalogue_app_error_component import (
            ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_created_by_component_error_component import (
            ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_created_by_user_error_component import (
            ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_criticality_error_component import (
            ApiV1KubernetesAppsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_debug_mode_error_component import (
            ApiV1KubernetesAppsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_description_error_component import (
            ApiV1KubernetesAppsUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_discovery_enabled_error_component import (
            ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_display_name_error_component import (
            ApiV1KubernetesAppsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_ha_enabled_error_component import (
            ApiV1KubernetesAppsUpdateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_helm_chart_error_component import (
            ApiV1KubernetesAppsUpdateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installation_failed_error_component import (
            ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installation_running_error_component import (
            ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installed_error_component import (
            ApiV1KubernetesAppsUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_installed_version_error_component import (
            ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_k8s_cluster_error_component import (
            ApiV1KubernetesAppsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_kind_error_component import (
            ApiV1KubernetesAppsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_labels_error_component import (
            ApiV1KubernetesAppsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_installation_error_component import (
            ApiV1KubernetesAppsUpdateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_metrics_check_error_component import (
            ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_modified_by_user_error_component import (
            ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_name_error_component import (
            ApiV1KubernetesAppsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_namespace_error_component import (
            ApiV1KubernetesAppsUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_non_field_errors_error_component import (
            ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_platform_service_error_component import (
            ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_available_error_component import (
            ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_details_error_component import (
            ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_ready_error_component import (
            ApiV1KubernetesAppsUpdatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_status_hash_error_component import (
            ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_total_error_component import (
            ApiV1KubernetesAppsUpdatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_pods_unavailable_error_component import (
            ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_error_component import (
            ApiV1KubernetesAppsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_id_error_component import (
            ApiV1KubernetesAppsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_provider_reference_error_component import (
            ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_scope_error_component import (
            ApiV1KubernetesAppsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_availability_error_component import (
            ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_target_error_component import (
            ApiV1KubernetesAppsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_sla_window_days_error_component import (
            ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_availability_error_component import (
            ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_target_error_component import (
            ApiV1KubernetesAppsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_slo_window_days_error_component import (
            ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_source_error_component import (
            ApiV1KubernetesAppsUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_target_availability_error_component import (
            ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstallation_running_error_component import (
            ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_update_uninstalled_error_component import (
            ApiV1KubernetesAppsUpdateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsUpdateActiveErrorComponent
                | ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAppsUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAppsUpdateArchivedByErrorComponent
                | ApiV1KubernetesAppsUpdateArchivedErrorComponent
                | ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsUpdateArtifactErrorComponent
                | ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsUpdateBlockErrorComponent
                | ApiV1KubernetesAppsUpdateByoaErrorComponent
                | ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsUpdateCriticalityErrorComponent
                | ApiV1KubernetesAppsUpdateDebugModeErrorComponent
                | ApiV1KubernetesAppsUpdateDescriptionErrorComponent
                | ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsUpdateHaEnabledErrorComponent
                | ApiV1KubernetesAppsUpdateHelmChartErrorComponent
                | ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsUpdateInstalledErrorComponent
                | ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsUpdateK8SClusterErrorComponent
                | ApiV1KubernetesAppsUpdateKindErrorComponent
                | ApiV1KubernetesAppsUpdateLabelsErrorComponent
                | ApiV1KubernetesAppsUpdateLastInstallationErrorComponent
                | ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsUpdateNameErrorComponent
                | ApiV1KubernetesAppsUpdateNamespaceErrorComponent
                | ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsUpdatePodsReadyErrorComponent
                | ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsUpdatePodsTotalErrorComponent
                | ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsUpdateProviderErrorComponent
                | ApiV1KubernetesAppsUpdateProviderIdErrorComponent
                | ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsUpdateScopeErrorComponent
                | ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsUpdateSloTargetErrorComponent
                | ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsUpdateSourceErrorComponent
                | ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsUpdateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_0 = (
                        ApiV1KubernetesAppsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_1 = (
                        ApiV1KubernetesAppsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_2 = (
                        ApiV1KubernetesAppsUpdateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_3 = (
                        ApiV1KubernetesAppsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_4 = (
                        ApiV1KubernetesAppsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_5 = (
                        ApiV1KubernetesAppsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_6 = (
                        ApiV1KubernetesAppsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_7 = (
                        ApiV1KubernetesAppsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_8 = (
                        ApiV1KubernetesAppsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_9 = (
                        ApiV1KubernetesAppsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_10 = (
                        ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_11 = (
                        ApiV1KubernetesAppsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_12 = (
                        ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_13 = (
                        ApiV1KubernetesAppsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_14 = (
                        ApiV1KubernetesAppsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_15 = (
                        ApiV1KubernetesAppsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_16 = (
                        ApiV1KubernetesAppsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_17 = (
                        ApiV1KubernetesAppsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_18 = (
                        ApiV1KubernetesAppsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_19 = (
                        ApiV1KubernetesAppsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_20 = (
                        ApiV1KubernetesAppsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_21 = (
                        ApiV1KubernetesAppsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_22 = (
                        ApiV1KubernetesAppsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_23 = (
                        ApiV1KubernetesAppsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_24 = (
                        ApiV1KubernetesAppsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_25 = (
                        ApiV1KubernetesAppsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_26 = (
                        ApiV1KubernetesAppsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_27 = (
                        ApiV1KubernetesAppsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_28 = (
                        ApiV1KubernetesAppsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_29 = (
                        ApiV1KubernetesAppsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_30 = (
                        ApiV1KubernetesAppsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_31 = (
                        ApiV1KubernetesAppsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_32 = (
                        ApiV1KubernetesAppsUpdateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_33 = (
                        ApiV1KubernetesAppsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_34 = (
                        ApiV1KubernetesAppsUpdateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_35 = (
                        ApiV1KubernetesAppsUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_36 = (
                        ApiV1KubernetesAppsUpdateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_37 = (
                        ApiV1KubernetesAppsUpdateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_38 = (
                        ApiV1KubernetesAppsUpdateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_39 = (
                        ApiV1KubernetesAppsUpdateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_40 = (
                        ApiV1KubernetesAppsUpdateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_41 = (
                        ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_42 = (
                        ApiV1KubernetesAppsUpdateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_43 = (
                        ApiV1KubernetesAppsUpdateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_44 = (
                        ApiV1KubernetesAppsUpdateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_45 = (
                        ApiV1KubernetesAppsUpdateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_46 = (
                        ApiV1KubernetesAppsUpdatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_47 = (
                        ApiV1KubernetesAppsUpdatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_48 = (
                        ApiV1KubernetesAppsUpdatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_49 = (
                        ApiV1KubernetesAppsUpdatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_50 = (
                        ApiV1KubernetesAppsUpdatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_51 = (
                        ApiV1KubernetesAppsUpdatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_52 = (
                        ApiV1KubernetesAppsUpdatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_53 = (
                        ApiV1KubernetesAppsUpdatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_54 = (
                        ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_55 = (
                        ApiV1KubernetesAppsUpdateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_56 = (
                        ApiV1KubernetesAppsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_57 = (
                        ApiV1KubernetesAppsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_58 = (
                        ApiV1KubernetesAppsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_59 = (
                        ApiV1KubernetesAppsUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_60 = (
                        ApiV1KubernetesAppsUpdateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_61 = (
                        ApiV1KubernetesAppsUpdateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_62 = (
                        ApiV1KubernetesAppsUpdateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_update_error_type_63 = (
                        ApiV1KubernetesAppsUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_update_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_update_error_type_64 = (
                    ApiV1KubernetesAppsUpdateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_update_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_update_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_update_validation_error

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
