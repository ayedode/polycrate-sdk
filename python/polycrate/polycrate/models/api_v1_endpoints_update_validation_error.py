from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_update_actual_availability_error_component import (
        ApiV1EndpointsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_update_annotations_error_component import (
        ApiV1EndpointsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_update_archived_at_error_component import (
        ApiV1EndpointsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_update_archived_by_error_component import (
        ApiV1EndpointsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_update_archived_error_component import ApiV1EndpointsUpdateArchivedErrorComponent
    from ..models.api_v1_endpoints_update_archived_reason_error_component import (
        ApiV1EndpointsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_update_check_result_retention_days_error_component import (
        ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_update_check_results_error_component import (
        ApiV1EndpointsUpdateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_update_created_by_component_error_component import (
        ApiV1EndpointsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_update_created_by_user_error_component import (
        ApiV1EndpointsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_update_criticality_error_component import (
        ApiV1EndpointsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_update_debug_mode_error_component import ApiV1EndpointsUpdateDebugModeErrorComponent
    from ..models.api_v1_endpoints_update_discovery_enabled_error_component import (
        ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_update_display_name_error_component import (
        ApiV1EndpointsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_update_do_not_monitor_error_component import (
        ApiV1EndpointsUpdateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_update_k8s_app_error_component import ApiV1EndpointsUpdateK8SAppErrorComponent
    from ..models.api_v1_endpoints_update_k8s_cluster_error_component import (
        ApiV1EndpointsUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_update_kind_error_component import ApiV1EndpointsUpdateKindErrorComponent
    from ..models.api_v1_endpoints_update_labels_error_component import ApiV1EndpointsUpdateLabelsErrorComponent
    from ..models.api_v1_endpoints_update_last_agent_metrics_error_component import (
        ApiV1EndpointsUpdateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_update_loadbalancer_instance_error_component import (
        ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_update_managed_by_content_type_error_component import (
        ApiV1EndpointsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_update_managed_by_object_id_error_component import (
        ApiV1EndpointsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_update_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_update_modified_by_user_error_component import (
        ApiV1EndpointsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_update_name_error_component import ApiV1EndpointsUpdateNameErrorComponent
    from ..models.api_v1_endpoints_update_non_field_errors_error_component import (
        ApiV1EndpointsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_update_organization_id_error_component import (
        ApiV1EndpointsUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_update_platform_dns_record_created_error_component import (
        ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_update_platform_service_error_component import (
        ApiV1EndpointsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_update_pop_endpoint_error_component import (
        ApiV1EndpointsUpdatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_update_provider_error_component import ApiV1EndpointsUpdateProviderErrorComponent
    from ..models.api_v1_endpoints_update_provider_id_error_component import (
        ApiV1EndpointsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_update_provider_reference_error_component import (
        ApiV1EndpointsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_update_reconciliation_enabled_error_component import (
        ApiV1EndpointsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_update_region_error_component import ApiV1EndpointsUpdateRegionErrorComponent
    from ..models.api_v1_endpoints_update_remote_address_error_component import (
        ApiV1EndpointsUpdateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_update_remote_port_error_component import (
        ApiV1EndpointsUpdateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_update_resolved_ip_error_component import (
        ApiV1EndpointsUpdateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_update_s3_cluster_error_component import ApiV1EndpointsUpdateS3ClusterErrorComponent
    from ..models.api_v1_endpoints_update_scope_error_component import ApiV1EndpointsUpdateScopeErrorComponent
    from ..models.api_v1_endpoints_update_sla_availability_error_component import (
        ApiV1EndpointsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_update_sla_target_error_component import ApiV1EndpointsUpdateSlaTargetErrorComponent
    from ..models.api_v1_endpoints_update_sla_window_days_error_component import (
        ApiV1EndpointsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_update_slo_availability_error_component import (
        ApiV1EndpointsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_update_slo_target_error_component import ApiV1EndpointsUpdateSloTargetErrorComponent
    from ..models.api_v1_endpoints_update_slo_window_days_error_component import (
        ApiV1EndpointsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_update_spec_error_component import ApiV1EndpointsUpdateSpecErrorComponent
    from ..models.api_v1_endpoints_update_target_availability_error_component import (
        ApiV1EndpointsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_update_workspace_id_error_component import (
        ApiV1EndpointsUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsUpdateValidationError")


@_attrs_define
class ApiV1EndpointsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsUpdateActualAvailabilityErrorComponent |
            ApiV1EndpointsUpdateAnnotationsErrorComponent | ApiV1EndpointsUpdateArchivedAtErrorComponent |
            ApiV1EndpointsUpdateArchivedByErrorComponent | ApiV1EndpointsUpdateArchivedErrorComponent |
            ApiV1EndpointsUpdateArchivedReasonErrorComponent | ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsUpdateCheckResultsErrorComponent | ApiV1EndpointsUpdateCreatedByComponentErrorComponent |
            ApiV1EndpointsUpdateCreatedByUserErrorComponent | ApiV1EndpointsUpdateCriticalityErrorComponent |
            ApiV1EndpointsUpdateDebugModeErrorComponent | ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsUpdateDisplayNameErrorComponent | ApiV1EndpointsUpdateDoNotMonitorErrorComponent |
            ApiV1EndpointsUpdateK8SAppErrorComponent | ApiV1EndpointsUpdateK8SClusterErrorComponent |
            ApiV1EndpointsUpdateKindErrorComponent | ApiV1EndpointsUpdateLabelsErrorComponent |
            ApiV1EndpointsUpdateLastAgentMetricsErrorComponent |
            ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent | ApiV1EndpointsUpdateManagedByContentTypeErrorComponent
            | ApiV1EndpointsUpdateManagedByObjectIdErrorComponent | ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsUpdateModifiedByUserErrorComponent | ApiV1EndpointsUpdateNameErrorComponent |
            ApiV1EndpointsUpdateNonFieldErrorsErrorComponent | ApiV1EndpointsUpdateOrganizationIdErrorComponent |
            ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent | ApiV1EndpointsUpdatePlatformServiceErrorComponent |
            ApiV1EndpointsUpdatePopEndpointErrorComponent | ApiV1EndpointsUpdateProviderErrorComponent |
            ApiV1EndpointsUpdateProviderIdErrorComponent | ApiV1EndpointsUpdateProviderReferenceErrorComponent |
            ApiV1EndpointsUpdateReconciliationEnabledErrorComponent | ApiV1EndpointsUpdateRegionErrorComponent |
            ApiV1EndpointsUpdateRemoteAddressErrorComponent | ApiV1EndpointsUpdateRemotePortErrorComponent |
            ApiV1EndpointsUpdateResolvedIpErrorComponent | ApiV1EndpointsUpdateS3ClusterErrorComponent |
            ApiV1EndpointsUpdateScopeErrorComponent | ApiV1EndpointsUpdateSlaAvailabilityErrorComponent |
            ApiV1EndpointsUpdateSlaTargetErrorComponent | ApiV1EndpointsUpdateSlaWindowDaysErrorComponent |
            ApiV1EndpointsUpdateSloAvailabilityErrorComponent | ApiV1EndpointsUpdateSloTargetErrorComponent |
            ApiV1EndpointsUpdateSloWindowDaysErrorComponent | ApiV1EndpointsUpdateSpecErrorComponent |
            ApiV1EndpointsUpdateTargetAvailabilityErrorComponent | ApiV1EndpointsUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsUpdateActualAvailabilityErrorComponent
        | ApiV1EndpointsUpdateAnnotationsErrorComponent
        | ApiV1EndpointsUpdateArchivedAtErrorComponent
        | ApiV1EndpointsUpdateArchivedByErrorComponent
        | ApiV1EndpointsUpdateArchivedErrorComponent
        | ApiV1EndpointsUpdateArchivedReasonErrorComponent
        | ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsUpdateCheckResultsErrorComponent
        | ApiV1EndpointsUpdateCreatedByComponentErrorComponent
        | ApiV1EndpointsUpdateCreatedByUserErrorComponent
        | ApiV1EndpointsUpdateCriticalityErrorComponent
        | ApiV1EndpointsUpdateDebugModeErrorComponent
        | ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsUpdateDisplayNameErrorComponent
        | ApiV1EndpointsUpdateDoNotMonitorErrorComponent
        | ApiV1EndpointsUpdateK8SAppErrorComponent
        | ApiV1EndpointsUpdateK8SClusterErrorComponent
        | ApiV1EndpointsUpdateKindErrorComponent
        | ApiV1EndpointsUpdateLabelsErrorComponent
        | ApiV1EndpointsUpdateLastAgentMetricsErrorComponent
        | ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsUpdateManagedByContentTypeErrorComponent
        | ApiV1EndpointsUpdateManagedByObjectIdErrorComponent
        | ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsUpdateModifiedByUserErrorComponent
        | ApiV1EndpointsUpdateNameErrorComponent
        | ApiV1EndpointsUpdateNonFieldErrorsErrorComponent
        | ApiV1EndpointsUpdateOrganizationIdErrorComponent
        | ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsUpdatePlatformServiceErrorComponent
        | ApiV1EndpointsUpdatePopEndpointErrorComponent
        | ApiV1EndpointsUpdateProviderErrorComponent
        | ApiV1EndpointsUpdateProviderIdErrorComponent
        | ApiV1EndpointsUpdateProviderReferenceErrorComponent
        | ApiV1EndpointsUpdateReconciliationEnabledErrorComponent
        | ApiV1EndpointsUpdateRegionErrorComponent
        | ApiV1EndpointsUpdateRemoteAddressErrorComponent
        | ApiV1EndpointsUpdateRemotePortErrorComponent
        | ApiV1EndpointsUpdateResolvedIpErrorComponent
        | ApiV1EndpointsUpdateS3ClusterErrorComponent
        | ApiV1EndpointsUpdateScopeErrorComponent
        | ApiV1EndpointsUpdateSlaAvailabilityErrorComponent
        | ApiV1EndpointsUpdateSlaTargetErrorComponent
        | ApiV1EndpointsUpdateSlaWindowDaysErrorComponent
        | ApiV1EndpointsUpdateSloAvailabilityErrorComponent
        | ApiV1EndpointsUpdateSloTargetErrorComponent
        | ApiV1EndpointsUpdateSloWindowDaysErrorComponent
        | ApiV1EndpointsUpdateSpecErrorComponent
        | ApiV1EndpointsUpdateTargetAvailabilityErrorComponent
        | ApiV1EndpointsUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_update_actual_availability_error_component import (
            ApiV1EndpointsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_annotations_error_component import (
            ApiV1EndpointsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_at_error_component import (
            ApiV1EndpointsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_by_error_component import (
            ApiV1EndpointsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_error_component import (
            ApiV1EndpointsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_reason_error_component import (
            ApiV1EndpointsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_check_result_retention_days_error_component import (
            ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_check_results_error_component import (
            ApiV1EndpointsUpdateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_created_by_component_error_component import (
            ApiV1EndpointsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_created_by_user_error_component import (
            ApiV1EndpointsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_criticality_error_component import (
            ApiV1EndpointsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_debug_mode_error_component import (
            ApiV1EndpointsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_discovery_enabled_error_component import (
            ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_display_name_error_component import (
            ApiV1EndpointsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_do_not_monitor_error_component import (
            ApiV1EndpointsUpdateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_k8s_app_error_component import (
            ApiV1EndpointsUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_k8s_cluster_error_component import (
            ApiV1EndpointsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_kind_error_component import (
            ApiV1EndpointsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_labels_error_component import (
            ApiV1EndpointsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_last_agent_metrics_error_component import (
            ApiV1EndpointsUpdateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_managed_by_content_type_error_component import (
            ApiV1EndpointsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_managed_by_object_id_error_component import (
            ApiV1EndpointsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_modified_by_user_error_component import (
            ApiV1EndpointsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_name_error_component import (
            ApiV1EndpointsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_non_field_errors_error_component import (
            ApiV1EndpointsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_organization_id_error_component import (
            ApiV1EndpointsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_platform_dns_record_created_error_component import (
            ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_platform_service_error_component import (
            ApiV1EndpointsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_pop_endpoint_error_component import (
            ApiV1EndpointsUpdatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_error_component import (
            ApiV1EndpointsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_id_error_component import (
            ApiV1EndpointsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_reference_error_component import (
            ApiV1EndpointsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_reconciliation_enabled_error_component import (
            ApiV1EndpointsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_region_error_component import (
            ApiV1EndpointsUpdateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_remote_address_error_component import (
            ApiV1EndpointsUpdateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_remote_port_error_component import (
            ApiV1EndpointsUpdateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_resolved_ip_error_component import (
            ApiV1EndpointsUpdateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_s3_cluster_error_component import (
            ApiV1EndpointsUpdateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_scope_error_component import (
            ApiV1EndpointsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_availability_error_component import (
            ApiV1EndpointsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_target_error_component import (
            ApiV1EndpointsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_window_days_error_component import (
            ApiV1EndpointsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_availability_error_component import (
            ApiV1EndpointsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_target_error_component import (
            ApiV1EndpointsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_window_days_error_component import (
            ApiV1EndpointsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_spec_error_component import (
            ApiV1EndpointsUpdateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_target_availability_error_component import (
            ApiV1EndpointsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_workspace_id_error_component import (
            ApiV1EndpointsUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsUpdateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_update_actual_availability_error_component import (
            ApiV1EndpointsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_annotations_error_component import (
            ApiV1EndpointsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_at_error_component import (
            ApiV1EndpointsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_by_error_component import (
            ApiV1EndpointsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_error_component import (
            ApiV1EndpointsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_archived_reason_error_component import (
            ApiV1EndpointsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_check_result_retention_days_error_component import (
            ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_check_results_error_component import (
            ApiV1EndpointsUpdateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_created_by_component_error_component import (
            ApiV1EndpointsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_created_by_user_error_component import (
            ApiV1EndpointsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_criticality_error_component import (
            ApiV1EndpointsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_debug_mode_error_component import (
            ApiV1EndpointsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_discovery_enabled_error_component import (
            ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_display_name_error_component import (
            ApiV1EndpointsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_do_not_monitor_error_component import (
            ApiV1EndpointsUpdateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_k8s_app_error_component import (
            ApiV1EndpointsUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_k8s_cluster_error_component import (
            ApiV1EndpointsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_kind_error_component import (
            ApiV1EndpointsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_labels_error_component import (
            ApiV1EndpointsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_last_agent_metrics_error_component import (
            ApiV1EndpointsUpdateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_loadbalancer_instance_error_component import (
            ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_managed_by_content_type_error_component import (
            ApiV1EndpointsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_managed_by_object_id_error_component import (
            ApiV1EndpointsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_modified_by_user_error_component import (
            ApiV1EndpointsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_name_error_component import (
            ApiV1EndpointsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_non_field_errors_error_component import (
            ApiV1EndpointsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_organization_id_error_component import (
            ApiV1EndpointsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_platform_dns_record_created_error_component import (
            ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_platform_service_error_component import (
            ApiV1EndpointsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_pop_endpoint_error_component import (
            ApiV1EndpointsUpdatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_error_component import (
            ApiV1EndpointsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_id_error_component import (
            ApiV1EndpointsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_provider_reference_error_component import (
            ApiV1EndpointsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_reconciliation_enabled_error_component import (
            ApiV1EndpointsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_region_error_component import (
            ApiV1EndpointsUpdateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_remote_address_error_component import (
            ApiV1EndpointsUpdateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_remote_port_error_component import (
            ApiV1EndpointsUpdateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_resolved_ip_error_component import (
            ApiV1EndpointsUpdateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_s3_cluster_error_component import (
            ApiV1EndpointsUpdateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_scope_error_component import (
            ApiV1EndpointsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_availability_error_component import (
            ApiV1EndpointsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_target_error_component import (
            ApiV1EndpointsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_sla_window_days_error_component import (
            ApiV1EndpointsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_availability_error_component import (
            ApiV1EndpointsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_target_error_component import (
            ApiV1EndpointsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_slo_window_days_error_component import (
            ApiV1EndpointsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_spec_error_component import (
            ApiV1EndpointsUpdateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_target_availability_error_component import (
            ApiV1EndpointsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_update_workspace_id_error_component import (
            ApiV1EndpointsUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsUpdateActualAvailabilityErrorComponent
                | ApiV1EndpointsUpdateAnnotationsErrorComponent
                | ApiV1EndpointsUpdateArchivedAtErrorComponent
                | ApiV1EndpointsUpdateArchivedByErrorComponent
                | ApiV1EndpointsUpdateArchivedErrorComponent
                | ApiV1EndpointsUpdateArchivedReasonErrorComponent
                | ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsUpdateCheckResultsErrorComponent
                | ApiV1EndpointsUpdateCreatedByComponentErrorComponent
                | ApiV1EndpointsUpdateCreatedByUserErrorComponent
                | ApiV1EndpointsUpdateCriticalityErrorComponent
                | ApiV1EndpointsUpdateDebugModeErrorComponent
                | ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsUpdateDisplayNameErrorComponent
                | ApiV1EndpointsUpdateDoNotMonitorErrorComponent
                | ApiV1EndpointsUpdateK8SAppErrorComponent
                | ApiV1EndpointsUpdateK8SClusterErrorComponent
                | ApiV1EndpointsUpdateKindErrorComponent
                | ApiV1EndpointsUpdateLabelsErrorComponent
                | ApiV1EndpointsUpdateLastAgentMetricsErrorComponent
                | ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsUpdateManagedByContentTypeErrorComponent
                | ApiV1EndpointsUpdateManagedByObjectIdErrorComponent
                | ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsUpdateModifiedByUserErrorComponent
                | ApiV1EndpointsUpdateNameErrorComponent
                | ApiV1EndpointsUpdateNonFieldErrorsErrorComponent
                | ApiV1EndpointsUpdateOrganizationIdErrorComponent
                | ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsUpdatePlatformServiceErrorComponent
                | ApiV1EndpointsUpdatePopEndpointErrorComponent
                | ApiV1EndpointsUpdateProviderErrorComponent
                | ApiV1EndpointsUpdateProviderIdErrorComponent
                | ApiV1EndpointsUpdateProviderReferenceErrorComponent
                | ApiV1EndpointsUpdateReconciliationEnabledErrorComponent
                | ApiV1EndpointsUpdateRegionErrorComponent
                | ApiV1EndpointsUpdateRemoteAddressErrorComponent
                | ApiV1EndpointsUpdateRemotePortErrorComponent
                | ApiV1EndpointsUpdateResolvedIpErrorComponent
                | ApiV1EndpointsUpdateS3ClusterErrorComponent
                | ApiV1EndpointsUpdateScopeErrorComponent
                | ApiV1EndpointsUpdateSlaAvailabilityErrorComponent
                | ApiV1EndpointsUpdateSlaTargetErrorComponent
                | ApiV1EndpointsUpdateSlaWindowDaysErrorComponent
                | ApiV1EndpointsUpdateSloAvailabilityErrorComponent
                | ApiV1EndpointsUpdateSloTargetErrorComponent
                | ApiV1EndpointsUpdateSloWindowDaysErrorComponent
                | ApiV1EndpointsUpdateSpecErrorComponent
                | ApiV1EndpointsUpdateTargetAvailabilityErrorComponent
                | ApiV1EndpointsUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_0 = (
                        ApiV1EndpointsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_1 = (
                        ApiV1EndpointsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_2 = (
                        ApiV1EndpointsUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_3 = (
                        ApiV1EndpointsUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_4 = (
                        ApiV1EndpointsUpdateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_5 = (
                        ApiV1EndpointsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_6 = (
                        ApiV1EndpointsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_7 = (
                        ApiV1EndpointsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_8 = (
                        ApiV1EndpointsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_9 = (
                        ApiV1EndpointsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_10 = (
                        ApiV1EndpointsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_11 = (
                        ApiV1EndpointsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_12 = (
                        ApiV1EndpointsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_13 = (
                        ApiV1EndpointsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_14 = (
                        ApiV1EndpointsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_15 = (
                        ApiV1EndpointsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_16 = (
                        ApiV1EndpointsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_17 = (
                        ApiV1EndpointsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_18 = (
                        ApiV1EndpointsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_19 = (
                        ApiV1EndpointsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_20 = (
                        ApiV1EndpointsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_21 = (
                        ApiV1EndpointsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_22 = (
                        ApiV1EndpointsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_23 = (
                        ApiV1EndpointsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_24 = (
                        ApiV1EndpointsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_25 = (
                        ApiV1EndpointsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_26 = (
                        ApiV1EndpointsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_27 = (
                        ApiV1EndpointsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_28 = (
                        ApiV1EndpointsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_29 = (
                        ApiV1EndpointsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_30 = (
                        ApiV1EndpointsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_31 = (
                        ApiV1EndpointsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_32 = (
                        ApiV1EndpointsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_33 = (
                        ApiV1EndpointsUpdateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_34 = (
                        ApiV1EndpointsUpdateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_35 = (
                        ApiV1EndpointsUpdateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_36 = (
                        ApiV1EndpointsUpdateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_37 = (
                        ApiV1EndpointsUpdatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_38 = (
                        ApiV1EndpointsUpdateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_39 = (
                        ApiV1EndpointsUpdateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_40 = (
                        ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_41 = (
                        ApiV1EndpointsUpdateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_42 = (
                        ApiV1EndpointsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_43 = (
                        ApiV1EndpointsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_44 = (
                        ApiV1EndpointsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_45 = (
                        ApiV1EndpointsUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_46 = (
                        ApiV1EndpointsUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_47 = (
                        ApiV1EndpointsUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_48 = (
                        ApiV1EndpointsUpdateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_update_error_type_49 = (
                        ApiV1EndpointsUpdateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_update_error_type_50 = (
                    ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_update_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_update_validation_error.additional_properties = d
        return api_v1_endpoints_update_validation_error

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
