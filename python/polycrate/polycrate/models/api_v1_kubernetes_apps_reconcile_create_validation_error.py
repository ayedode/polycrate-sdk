from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_reconcile_create_active_error_component import (
        ApiV1KubernetesAppsReconcileCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_actual_availability_error_component import (
        ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_annotations_error_component import (
        ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_archived_at_error_component import (
        ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_archived_by_error_component import (
        ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_archived_error_component import (
        ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_archived_reason_error_component import (
        ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_error_component import (
        ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_package_error_component import (
        ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_block_error_component import (
        ApiV1KubernetesAppsReconcileCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_byoa_error_component import (
        ApiV1KubernetesAppsReconcileCreateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_component_error_component import (
        ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_user_error_component import (
        ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_criticality_error_component import (
        ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_debug_mode_error_component import (
        ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_description_error_component import (
        ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_display_name_error_component import (
        ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_helm_chart_error_component import (
        ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_installation_failed_error_component import (
        ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_installation_running_error_component import (
        ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_installed_error_component import (
        ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_installed_version_error_component import (
        ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_kind_error_component import (
        ApiV1KubernetesAppsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_labels_error_component import (
        ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_last_installation_error_component import (
        ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_name_error_component import (
        ApiV1KubernetesAppsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_namespace_error_component import (
        ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_platform_service_error_component import (
        ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_available_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_details_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_ready_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_total_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_provider_error_component import (
        ApiV1KubernetesAppsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_provider_id_error_component import (
        ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_provider_reference_error_component import (
        ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_scope_error_component import (
        ApiV1KubernetesAppsReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_sla_availability_error_component import (
        ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_sla_target_error_component import (
        ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_slo_availability_error_component import (
        ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_slo_target_error_component import (
        ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_source_error_component import (
        ApiV1KubernetesAppsReconcileCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_target_availability_error_component import (
        ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_reconcile_create_uninstalled_error_component import (
        ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsReconcileCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsReconcileCreateActiveErrorComponent |
            ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent |
            ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsReconcileCreateBlockErrorComponent | ApiV1KubernetesAppsReconcileCreateByoaErrorComponent |
            ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent |
            ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent |
            ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent |
            ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent |
            ApiV1KubernetesAppsReconcileCreateKindErrorComponent | ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent |
            ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsReconcileCreateNameErrorComponent | ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent
            | ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsReconcileCreateProviderErrorComponent |
            ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent |
            ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsReconcileCreateScopeErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsReconcileCreateSourceErrorComponent |
            ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsReconcileCreateActiveErrorComponent
        | ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent
        | ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsReconcileCreateBlockErrorComponent
        | ApiV1KubernetesAppsReconcileCreateByoaErrorComponent
        | ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent
        | ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsReconcileCreateKindErrorComponent
        | ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent
        | ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsReconcileCreateNameErrorComponent
        | ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsReconcileCreateProviderErrorComponent
        | ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsReconcileCreateScopeErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsReconcileCreateSourceErrorComponent
        | ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_reconcile_create_active_error_component import (
            ApiV1KubernetesAppsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_actual_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_annotations_error_component import (
            ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_at_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_by_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_reason_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_error_component import (
            ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_package_error_component import (
            ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_block_error_component import (
            ApiV1KubernetesAppsReconcileCreateBlockErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_byoa_error_component import (
            ApiV1KubernetesAppsReconcileCreateByoaErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_component_error_component import (
            ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_user_error_component import (
            ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_criticality_error_component import (
            ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_debug_mode_error_component import (
            ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_description_error_component import (
            ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_display_name_error_component import (
            ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_helm_chart_error_component import (
            ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installation_failed_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installation_running_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installed_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installed_version_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_kind_error_component import (
            ApiV1KubernetesAppsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_labels_error_component import (
            ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_installation_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_name_error_component import (
            ApiV1KubernetesAppsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_namespace_error_component import (
            ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_platform_service_error_component import (
            ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_available_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_details_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_ready_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_total_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_id_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_reference_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_scope_error_component import (
            ApiV1KubernetesAppsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_target_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_target_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_source_error_component import (
            ApiV1KubernetesAppsReconcileCreateSourceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_target_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstalled_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_reconcile_create_active_error_component import (
            ApiV1KubernetesAppsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_actual_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_annotations_error_component import (
            ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_at_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_by_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_archived_reason_error_component import (
            ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_error_component import (
            ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_artifact_package_error_component import (
            ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_block_error_component import (
            ApiV1KubernetesAppsReconcileCreateBlockErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_byoa_error_component import (
            ApiV1KubernetesAppsReconcileCreateByoaErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_component_error_component import (
            ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_created_by_user_error_component import (
            ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_criticality_error_component import (
            ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_debug_mode_error_component import (
            ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_description_error_component import (
            ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_display_name_error_component import (
            ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_helm_chart_error_component import (
            ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installation_failed_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installation_running_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installed_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_installed_version_error_component import (
            ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_kind_error_component import (
            ApiV1KubernetesAppsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_labels_error_component import (
            ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_installation_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_name_error_component import (
            ApiV1KubernetesAppsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_namespace_error_component import (
            ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_platform_service_error_component import (
            ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_available_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_details_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_ready_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_total_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_id_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_provider_reference_error_component import (
            ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_scope_error_component import (
            ApiV1KubernetesAppsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_target_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_target_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_source_error_component import (
            ApiV1KubernetesAppsReconcileCreateSourceErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_target_availability_error_component import (
            ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent,
        )
        from ..models.api_v1_kubernetes_apps_reconcile_create_uninstalled_error_component import (
            ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsReconcileCreateActiveErrorComponent
                | ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent
                | ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsReconcileCreateBlockErrorComponent
                | ApiV1KubernetesAppsReconcileCreateByoaErrorComponent
                | ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent
                | ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsReconcileCreateKindErrorComponent
                | ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent
                | ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsReconcileCreateNameErrorComponent
                | ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsReconcileCreateProviderErrorComponent
                | ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsReconcileCreateScopeErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsReconcileCreateSourceErrorComponent
                | ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_0 = (
                        ApiV1KubernetesAppsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_1 = (
                        ApiV1KubernetesAppsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_2 = (
                        ApiV1KubernetesAppsReconcileCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_3 = (
                        ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_4 = (
                        ApiV1KubernetesAppsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_5 = (
                        ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_6 = (
                        ApiV1KubernetesAppsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_7 = (
                        ApiV1KubernetesAppsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_8 = (
                        ApiV1KubernetesAppsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_9 = (
                        ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_10 = (
                        ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_11 = (
                        ApiV1KubernetesAppsReconcileCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_12 = (
                        ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_13 = (
                        ApiV1KubernetesAppsReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_14 = (
                        ApiV1KubernetesAppsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_15 = (
                        ApiV1KubernetesAppsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_16 = (
                        ApiV1KubernetesAppsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_17 = (
                        ApiV1KubernetesAppsReconcileCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_18 = (
                        ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_19 = (
                        ApiV1KubernetesAppsReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_20 = (
                        ApiV1KubernetesAppsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_21 = (
                        ApiV1KubernetesAppsReconcileCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_22 = (
                        ApiV1KubernetesAppsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_23 = (
                        ApiV1KubernetesAppsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_24 = (
                        ApiV1KubernetesAppsReconcileCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_25 = (
                        ApiV1KubernetesAppsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_26 = (
                        ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_27 = (
                        ApiV1KubernetesAppsReconcileCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_28 = (
                        ApiV1KubernetesAppsReconcileCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_29 = (
                        ApiV1KubernetesAppsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_30 = (
                        ApiV1KubernetesAppsReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_31 = (
                        ApiV1KubernetesAppsReconcileCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_32 = (
                        ApiV1KubernetesAppsReconcileCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_33 = (
                        ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_34 = (
                        ApiV1KubernetesAppsReconcileCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_35 = (
                        ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_36 = (
                        ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_37 = (
                        ApiV1KubernetesAppsReconcileCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_38 = (
                        ApiV1KubernetesAppsReconcileCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_39 = (
                        ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_40 = (
                        ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_41 = (
                        ApiV1KubernetesAppsReconcileCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_42 = (
                        ApiV1KubernetesAppsReconcileCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_43 = (
                        ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_44 = (
                        ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_45 = (
                        ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_46 = (
                        ApiV1KubernetesAppsReconcileCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_47 = (
                        ApiV1KubernetesAppsReconcileCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_48 = (
                        ApiV1KubernetesAppsReconcileCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_49 = (
                        ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_50 = (
                        ApiV1KubernetesAppsReconcileCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_51 = (
                        ApiV1KubernetesAppsReconcileCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_52 = (
                        ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_53 = (
                        ApiV1KubernetesAppsReconcileCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_54 = (
                        ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_55 = (
                        ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_56 = (
                        ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_57 = (
                        ApiV1KubernetesAppsReconcileCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_58 = (
                        ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_59 = (
                        ApiV1KubernetesAppsReconcileCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_60 = (
                        ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_61 = (
                        ApiV1KubernetesAppsReconcileCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_62 = (
                        ApiV1KubernetesAppsReconcileCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_63 = (
                        ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_64 = (
                    ApiV1KubernetesAppsReconcileCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_reconcile_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_reconcile_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_reconcile_create_validation_error

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
