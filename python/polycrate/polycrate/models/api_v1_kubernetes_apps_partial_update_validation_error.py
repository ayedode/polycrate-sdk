from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_partial_update_active_error_component import (
        ApiV1KubernetesAppsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_actual_availability_error_component import (
        ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_annotations_error_component import (
        ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_archived_at_error_component import (
        ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_archived_by_error_component import (
        ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_archived_error_component import (
        ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_archived_reason_error_component import (
        ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_artifact_error_component import (
        ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_artifact_package_error_component import (
        ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_block_error_component import (
        ApiV1KubernetesAppsPartialUpdateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_byoa_error_component import (
        ApiV1KubernetesAppsPartialUpdateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_catalogue_app_error_component import (
        ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_created_by_component_error_component import (
        ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_created_by_user_error_component import (
        ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_criticality_error_component import (
        ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_debug_mode_error_component import (
        ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_description_error_component import (
        ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_display_name_error_component import (
        ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_ha_enabled_error_component import (
        ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_helm_chart_error_component import (
        ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_installation_failed_error_component import (
        ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_installation_running_error_component import (
        ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_installed_error_component import (
        ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_installed_version_error_component import (
        ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_k8s_cluster_error_component import (
        ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_kind_error_component import (
        ApiV1KubernetesAppsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_labels_error_component import (
        ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_last_installation_error_component import (
        ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_last_metrics_check_error_component import (
        ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_modified_by_user_error_component import (
        ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_name_error_component import (
        ApiV1KubernetesAppsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_namespace_error_component import (
        ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_platform_service_error_component import (
        ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_available_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_details_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_ready_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_status_hash_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_total_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_pods_unavailable_error_component import (
        ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_provider_error_component import (
        ApiV1KubernetesAppsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_provider_id_error_component import (
        ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_provider_reference_error_component import (
        ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_scope_error_component import (
        ApiV1KubernetesAppsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_sla_availability_error_component import (
        ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_sla_target_error_component import (
        ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_sla_window_days_error_component import (
        ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_slo_availability_error_component import (
        ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_slo_target_error_component import (
        ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_slo_window_days_error_component import (
        ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_source_error_component import (
        ApiV1KubernetesAppsPartialUpdateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_target_availability_error_component import (
        ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_running_error_component import (
        ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_partial_update_uninstalled_error_component import (
        ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAppsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsPartialUpdateActiveErrorComponent |
            ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent |
            ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsPartialUpdateBlockErrorComponent | ApiV1KubernetesAppsPartialUpdateByoaErrorComponent |
            ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent |
            ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent |
            ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent |
            ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent |
            ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent | ApiV1KubernetesAppsPartialUpdateKindErrorComponent |
            ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent |
            ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsPartialUpdateNameErrorComponent | ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent |
            ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent |
            ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsPartialUpdateSourceErrorComponent |
            ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsPartialUpdateActiveErrorComponent
        | ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent
        | ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsPartialUpdateBlockErrorComponent
        | ApiV1KubernetesAppsPartialUpdateByoaErrorComponent
        | ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent
        | ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent
        | ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent
        | ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent
        | ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent
        | ApiV1KubernetesAppsPartialUpdateKindErrorComponent
        | ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent
        | ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsPartialUpdateNameErrorComponent
        | ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent
        | ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent
        | ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsPartialUpdateSourceErrorComponent
        | ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_partial_update_active_error_component import (
            ApiV1KubernetesAppsPartialUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_annotations_error_component import (
            ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_at_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_by_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_artifact_error_component import (
            ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_artifact_package_error_component import (
            ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_block_error_component import (
            ApiV1KubernetesAppsPartialUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_byoa_error_component import (
            ApiV1KubernetesAppsPartialUpdateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_catalogue_app_error_component import (
            ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_created_by_component_error_component import (
            ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_created_by_user_error_component import (
            ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_criticality_error_component import (
            ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_description_error_component import (
            ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_display_name_error_component import (
            ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_ha_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_helm_chart_error_component import (
            ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installation_failed_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installation_running_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installed_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installed_version_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_kind_error_component import (
            ApiV1KubernetesAppsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_labels_error_component import (
            ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_installation_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_metrics_check_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_modified_by_user_error_component import (
            ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_name_error_component import (
            ApiV1KubernetesAppsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_namespace_error_component import (
            ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_platform_service_error_component import (
            ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_available_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_details_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_ready_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_status_hash_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_total_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_unavailable_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_id_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_scope_error_component import (
            ApiV1KubernetesAppsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_target_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_window_days_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_target_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_window_days_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_source_error_component import (
            ApiV1KubernetesAppsPartialUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_target_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_running_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstalled_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_partial_update_active_error_component import (
            ApiV1KubernetesAppsPartialUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_annotations_error_component import (
            ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_at_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_by_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_artifact_error_component import (
            ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_artifact_package_error_component import (
            ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_block_error_component import (
            ApiV1KubernetesAppsPartialUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_byoa_error_component import (
            ApiV1KubernetesAppsPartialUpdateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_catalogue_app_error_component import (
            ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_created_by_component_error_component import (
            ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_created_by_user_error_component import (
            ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_criticality_error_component import (
            ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_description_error_component import (
            ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_display_name_error_component import (
            ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_ha_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_helm_chart_error_component import (
            ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installation_failed_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installation_running_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installed_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_installed_version_error_component import (
            ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_k8s_cluster_error_component import (
            ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_kind_error_component import (
            ApiV1KubernetesAppsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_labels_error_component import (
            ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_installation_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_metrics_check_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_modified_by_user_error_component import (
            ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_name_error_component import (
            ApiV1KubernetesAppsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_namespace_error_component import (
            ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_platform_service_error_component import (
            ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_available_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_details_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_ready_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_status_hash_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_total_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_pods_unavailable_error_component import (
            ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_id_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_scope_error_component import (
            ApiV1KubernetesAppsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_target_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_sla_window_days_error_component import (
            ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_target_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_slo_window_days_error_component import (
            ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_source_error_component import (
            ApiV1KubernetesAppsPartialUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_target_availability_error_component import (
            ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstallation_running_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_partial_update_uninstalled_error_component import (
            ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsPartialUpdateActiveErrorComponent
                | ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent
                | ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsPartialUpdateBlockErrorComponent
                | ApiV1KubernetesAppsPartialUpdateByoaErrorComponent
                | ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent
                | ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent
                | ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent
                | ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent
                | ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent
                | ApiV1KubernetesAppsPartialUpdateKindErrorComponent
                | ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent
                | ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsPartialUpdateNameErrorComponent
                | ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent
                | ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent
                | ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsPartialUpdateSourceErrorComponent
                | ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_0 = (
                        ApiV1KubernetesAppsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_1 = (
                        ApiV1KubernetesAppsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_2 = (
                        ApiV1KubernetesAppsPartialUpdateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_3 = (
                        ApiV1KubernetesAppsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_4 = (
                        ApiV1KubernetesAppsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_5 = (
                        ApiV1KubernetesAppsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_6 = (
                        ApiV1KubernetesAppsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_7 = (
                        ApiV1KubernetesAppsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_8 = (
                        ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_9 = (
                        ApiV1KubernetesAppsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_10 = (
                        ApiV1KubernetesAppsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_11 = (
                        ApiV1KubernetesAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_12 = (
                        ApiV1KubernetesAppsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_13 = (
                        ApiV1KubernetesAppsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_14 = (
                        ApiV1KubernetesAppsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_15 = (
                        ApiV1KubernetesAppsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_16 = (
                        ApiV1KubernetesAppsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_17 = (
                        ApiV1KubernetesAppsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_18 = (
                        ApiV1KubernetesAppsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_19 = (
                        ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_20 = (
                        ApiV1KubernetesAppsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_21 = (
                        ApiV1KubernetesAppsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_22 = (
                        ApiV1KubernetesAppsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_23 = (
                        ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_24 = (
                        ApiV1KubernetesAppsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_25 = (
                        ApiV1KubernetesAppsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_26 = (
                        ApiV1KubernetesAppsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_27 = (
                        ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_28 = (
                        ApiV1KubernetesAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_29 = (
                        ApiV1KubernetesAppsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_30 = (
                        ApiV1KubernetesAppsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_31 = (
                        ApiV1KubernetesAppsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_32 = (
                        ApiV1KubernetesAppsPartialUpdateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_33 = (
                        ApiV1KubernetesAppsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_34 = (
                        ApiV1KubernetesAppsPartialUpdateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_35 = (
                        ApiV1KubernetesAppsPartialUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_36 = (
                        ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_37 = (
                        ApiV1KubernetesAppsPartialUpdateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_38 = (
                        ApiV1KubernetesAppsPartialUpdateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_39 = (
                        ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_40 = (
                        ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_41 = (
                        ApiV1KubernetesAppsPartialUpdateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_42 = (
                        ApiV1KubernetesAppsPartialUpdateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_43 = (
                        ApiV1KubernetesAppsPartialUpdateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_44 = (
                        ApiV1KubernetesAppsPartialUpdateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_45 = (
                        ApiV1KubernetesAppsPartialUpdateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_46 = (
                        ApiV1KubernetesAppsPartialUpdatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_47 = (
                        ApiV1KubernetesAppsPartialUpdatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_48 = (
                        ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_49 = (
                        ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_50 = (
                        ApiV1KubernetesAppsPartialUpdatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_51 = (
                        ApiV1KubernetesAppsPartialUpdatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_52 = (
                        ApiV1KubernetesAppsPartialUpdatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_53 = (
                        ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_54 = (
                        ApiV1KubernetesAppsPartialUpdatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_55 = (
                        ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_56 = (
                        ApiV1KubernetesAppsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_57 = (
                        ApiV1KubernetesAppsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_58 = (
                        ApiV1KubernetesAppsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_59 = (
                        ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_60 = (
                        ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_61 = (
                        ApiV1KubernetesAppsPartialUpdateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_62 = (
                        ApiV1KubernetesAppsPartialUpdateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_63 = (
                        ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_64 = (
                    ApiV1KubernetesAppsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_partial_update_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_partial_update_validation_error

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
