from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_create_actual_availability_error_component import (
        ApiV1EndpointsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_create_annotations_error_component import (
        ApiV1EndpointsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_create_archived_at_error_component import (
        ApiV1EndpointsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_create_archived_by_error_component import (
        ApiV1EndpointsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_create_archived_error_component import ApiV1EndpointsCreateArchivedErrorComponent
    from ..models.api_v1_endpoints_create_archived_reason_error_component import (
        ApiV1EndpointsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_create_check_result_retention_days_error_component import (
        ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_create_check_results_error_component import (
        ApiV1EndpointsCreateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_create_created_by_component_error_component import (
        ApiV1EndpointsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_create_created_by_user_error_component import (
        ApiV1EndpointsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_create_criticality_error_component import (
        ApiV1EndpointsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_create_debug_mode_error_component import ApiV1EndpointsCreateDebugModeErrorComponent
    from ..models.api_v1_endpoints_create_discovery_enabled_error_component import (
        ApiV1EndpointsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_create_display_name_error_component import (
        ApiV1EndpointsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_create_do_not_monitor_error_component import (
        ApiV1EndpointsCreateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_create_k8s_app_error_component import ApiV1EndpointsCreateK8SAppErrorComponent
    from ..models.api_v1_endpoints_create_k8s_cluster_error_component import (
        ApiV1EndpointsCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_create_kind_error_component import ApiV1EndpointsCreateKindErrorComponent
    from ..models.api_v1_endpoints_create_labels_error_component import ApiV1EndpointsCreateLabelsErrorComponent
    from ..models.api_v1_endpoints_create_last_agent_metrics_error_component import (
        ApiV1EndpointsCreateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_create_loadbalancer_instance_error_component import (
        ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_create_managed_by_content_type_error_component import (
        ApiV1EndpointsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_create_managed_by_object_id_error_component import (
        ApiV1EndpointsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_create_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_create_modified_by_user_error_component import (
        ApiV1EndpointsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_create_name_error_component import ApiV1EndpointsCreateNameErrorComponent
    from ..models.api_v1_endpoints_create_non_field_errors_error_component import (
        ApiV1EndpointsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_create_organization_id_error_component import (
        ApiV1EndpointsCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_create_platform_dns_record_created_error_component import (
        ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_create_platform_service_error_component import (
        ApiV1EndpointsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_create_pop_endpoint_error_component import (
        ApiV1EndpointsCreatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_create_provider_error_component import ApiV1EndpointsCreateProviderErrorComponent
    from ..models.api_v1_endpoints_create_provider_id_error_component import (
        ApiV1EndpointsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_create_provider_reference_error_component import (
        ApiV1EndpointsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_create_reconciliation_enabled_error_component import (
        ApiV1EndpointsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_create_region_error_component import ApiV1EndpointsCreateRegionErrorComponent
    from ..models.api_v1_endpoints_create_remote_address_error_component import (
        ApiV1EndpointsCreateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_create_remote_port_error_component import (
        ApiV1EndpointsCreateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_create_resolved_ip_error_component import (
        ApiV1EndpointsCreateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_create_s3_cluster_error_component import ApiV1EndpointsCreateS3ClusterErrorComponent
    from ..models.api_v1_endpoints_create_scope_error_component import ApiV1EndpointsCreateScopeErrorComponent
    from ..models.api_v1_endpoints_create_sla_availability_error_component import (
        ApiV1EndpointsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_create_sla_target_error_component import ApiV1EndpointsCreateSlaTargetErrorComponent
    from ..models.api_v1_endpoints_create_sla_window_days_error_component import (
        ApiV1EndpointsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_create_slo_availability_error_component import (
        ApiV1EndpointsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_create_slo_target_error_component import ApiV1EndpointsCreateSloTargetErrorComponent
    from ..models.api_v1_endpoints_create_slo_window_days_error_component import (
        ApiV1EndpointsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_create_spec_error_component import ApiV1EndpointsCreateSpecErrorComponent
    from ..models.api_v1_endpoints_create_target_availability_error_component import (
        ApiV1EndpointsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_create_workspace_id_error_component import (
        ApiV1EndpointsCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsCreateValidationError")


@_attrs_define
class ApiV1EndpointsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsCreateActualAvailabilityErrorComponent |
            ApiV1EndpointsCreateAnnotationsErrorComponent | ApiV1EndpointsCreateArchivedAtErrorComponent |
            ApiV1EndpointsCreateArchivedByErrorComponent | ApiV1EndpointsCreateArchivedErrorComponent |
            ApiV1EndpointsCreateArchivedReasonErrorComponent | ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsCreateCheckResultsErrorComponent | ApiV1EndpointsCreateCreatedByComponentErrorComponent |
            ApiV1EndpointsCreateCreatedByUserErrorComponent | ApiV1EndpointsCreateCriticalityErrorComponent |
            ApiV1EndpointsCreateDebugModeErrorComponent | ApiV1EndpointsCreateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsCreateDisplayNameErrorComponent | ApiV1EndpointsCreateDoNotMonitorErrorComponent |
            ApiV1EndpointsCreateK8SAppErrorComponent | ApiV1EndpointsCreateK8SClusterErrorComponent |
            ApiV1EndpointsCreateKindErrorComponent | ApiV1EndpointsCreateLabelsErrorComponent |
            ApiV1EndpointsCreateLastAgentMetricsErrorComponent |
            ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent | ApiV1EndpointsCreateManagedByContentTypeErrorComponent
            | ApiV1EndpointsCreateManagedByObjectIdErrorComponent | ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsCreateModifiedByUserErrorComponent | ApiV1EndpointsCreateNameErrorComponent |
            ApiV1EndpointsCreateNonFieldErrorsErrorComponent | ApiV1EndpointsCreateOrganizationIdErrorComponent |
            ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent | ApiV1EndpointsCreatePlatformServiceErrorComponent |
            ApiV1EndpointsCreatePopEndpointErrorComponent | ApiV1EndpointsCreateProviderErrorComponent |
            ApiV1EndpointsCreateProviderIdErrorComponent | ApiV1EndpointsCreateProviderReferenceErrorComponent |
            ApiV1EndpointsCreateReconciliationEnabledErrorComponent | ApiV1EndpointsCreateRegionErrorComponent |
            ApiV1EndpointsCreateRemoteAddressErrorComponent | ApiV1EndpointsCreateRemotePortErrorComponent |
            ApiV1EndpointsCreateResolvedIpErrorComponent | ApiV1EndpointsCreateS3ClusterErrorComponent |
            ApiV1EndpointsCreateScopeErrorComponent | ApiV1EndpointsCreateSlaAvailabilityErrorComponent |
            ApiV1EndpointsCreateSlaTargetErrorComponent | ApiV1EndpointsCreateSlaWindowDaysErrorComponent |
            ApiV1EndpointsCreateSloAvailabilityErrorComponent | ApiV1EndpointsCreateSloTargetErrorComponent |
            ApiV1EndpointsCreateSloWindowDaysErrorComponent | ApiV1EndpointsCreateSpecErrorComponent |
            ApiV1EndpointsCreateTargetAvailabilityErrorComponent | ApiV1EndpointsCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsCreateActualAvailabilityErrorComponent
        | ApiV1EndpointsCreateAnnotationsErrorComponent
        | ApiV1EndpointsCreateArchivedAtErrorComponent
        | ApiV1EndpointsCreateArchivedByErrorComponent
        | ApiV1EndpointsCreateArchivedErrorComponent
        | ApiV1EndpointsCreateArchivedReasonErrorComponent
        | ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsCreateCheckResultsErrorComponent
        | ApiV1EndpointsCreateCreatedByComponentErrorComponent
        | ApiV1EndpointsCreateCreatedByUserErrorComponent
        | ApiV1EndpointsCreateCriticalityErrorComponent
        | ApiV1EndpointsCreateDebugModeErrorComponent
        | ApiV1EndpointsCreateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsCreateDisplayNameErrorComponent
        | ApiV1EndpointsCreateDoNotMonitorErrorComponent
        | ApiV1EndpointsCreateK8SAppErrorComponent
        | ApiV1EndpointsCreateK8SClusterErrorComponent
        | ApiV1EndpointsCreateKindErrorComponent
        | ApiV1EndpointsCreateLabelsErrorComponent
        | ApiV1EndpointsCreateLastAgentMetricsErrorComponent
        | ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsCreateManagedByContentTypeErrorComponent
        | ApiV1EndpointsCreateManagedByObjectIdErrorComponent
        | ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsCreateModifiedByUserErrorComponent
        | ApiV1EndpointsCreateNameErrorComponent
        | ApiV1EndpointsCreateNonFieldErrorsErrorComponent
        | ApiV1EndpointsCreateOrganizationIdErrorComponent
        | ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsCreatePlatformServiceErrorComponent
        | ApiV1EndpointsCreatePopEndpointErrorComponent
        | ApiV1EndpointsCreateProviderErrorComponent
        | ApiV1EndpointsCreateProviderIdErrorComponent
        | ApiV1EndpointsCreateProviderReferenceErrorComponent
        | ApiV1EndpointsCreateReconciliationEnabledErrorComponent
        | ApiV1EndpointsCreateRegionErrorComponent
        | ApiV1EndpointsCreateRemoteAddressErrorComponent
        | ApiV1EndpointsCreateRemotePortErrorComponent
        | ApiV1EndpointsCreateResolvedIpErrorComponent
        | ApiV1EndpointsCreateS3ClusterErrorComponent
        | ApiV1EndpointsCreateScopeErrorComponent
        | ApiV1EndpointsCreateSlaAvailabilityErrorComponent
        | ApiV1EndpointsCreateSlaTargetErrorComponent
        | ApiV1EndpointsCreateSlaWindowDaysErrorComponent
        | ApiV1EndpointsCreateSloAvailabilityErrorComponent
        | ApiV1EndpointsCreateSloTargetErrorComponent
        | ApiV1EndpointsCreateSloWindowDaysErrorComponent
        | ApiV1EndpointsCreateSpecErrorComponent
        | ApiV1EndpointsCreateTargetAvailabilityErrorComponent
        | ApiV1EndpointsCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_create_actual_availability_error_component import (
            ApiV1EndpointsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_annotations_error_component import (
            ApiV1EndpointsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_at_error_component import (
            ApiV1EndpointsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_by_error_component import (
            ApiV1EndpointsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_error_component import ApiV1EndpointsCreateArchivedErrorComponent
        from ..models.api_v1_endpoints_create_archived_reason_error_component import (
            ApiV1EndpointsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_create_check_result_retention_days_error_component import (
            ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_check_results_error_component import (
            ApiV1EndpointsCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_created_by_component_error_component import (
            ApiV1EndpointsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_create_created_by_user_error_component import (
            ApiV1EndpointsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_create_criticality_error_component import (
            ApiV1EndpointsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_debug_mode_error_component import (
            ApiV1EndpointsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_create_discovery_enabled_error_component import (
            ApiV1EndpointsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_create_display_name_error_component import (
            ApiV1EndpointsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_create_do_not_monitor_error_component import (
            ApiV1EndpointsCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_create_k8s_app_error_component import ApiV1EndpointsCreateK8SAppErrorComponent
        from ..models.api_v1_endpoints_create_k8s_cluster_error_component import (
            ApiV1EndpointsCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_create_kind_error_component import ApiV1EndpointsCreateKindErrorComponent
        from ..models.api_v1_endpoints_create_labels_error_component import ApiV1EndpointsCreateLabelsErrorComponent
        from ..models.api_v1_endpoints_create_last_agent_metrics_error_component import (
            ApiV1EndpointsCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_managed_by_content_type_error_component import (
            ApiV1EndpointsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_create_managed_by_object_id_error_component import (
            ApiV1EndpointsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_create_modified_by_user_error_component import (
            ApiV1EndpointsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_create_name_error_component import ApiV1EndpointsCreateNameErrorComponent
        from ..models.api_v1_endpoints_create_non_field_errors_error_component import (
            ApiV1EndpointsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_organization_id_error_component import (
            ApiV1EndpointsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_create_platform_service_error_component import (
            ApiV1EndpointsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_create_pop_endpoint_error_component import (
            ApiV1EndpointsCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_create_provider_error_component import ApiV1EndpointsCreateProviderErrorComponent
        from ..models.api_v1_endpoints_create_provider_id_error_component import (
            ApiV1EndpointsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_provider_reference_error_component import (
            ApiV1EndpointsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_create_region_error_component import ApiV1EndpointsCreateRegionErrorComponent
        from ..models.api_v1_endpoints_create_remote_address_error_component import (
            ApiV1EndpointsCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_create_remote_port_error_component import (
            ApiV1EndpointsCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_create_resolved_ip_error_component import (
            ApiV1EndpointsCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_create_s3_cluster_error_component import (
            ApiV1EndpointsCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_create_scope_error_component import ApiV1EndpointsCreateScopeErrorComponent
        from ..models.api_v1_endpoints_create_sla_availability_error_component import (
            ApiV1EndpointsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_sla_target_error_component import (
            ApiV1EndpointsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_create_sla_window_days_error_component import (
            ApiV1EndpointsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_availability_error_component import (
            ApiV1EndpointsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_target_error_component import (
            ApiV1EndpointsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_window_days_error_component import (
            ApiV1EndpointsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_spec_error_component import ApiV1EndpointsCreateSpecErrorComponent
        from ..models.api_v1_endpoints_create_target_availability_error_component import (
            ApiV1EndpointsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_workspace_id_error_component import (
            ApiV1EndpointsCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsCreateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_create_actual_availability_error_component import (
            ApiV1EndpointsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_annotations_error_component import (
            ApiV1EndpointsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_at_error_component import (
            ApiV1EndpointsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_by_error_component import (
            ApiV1EndpointsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_create_archived_error_component import ApiV1EndpointsCreateArchivedErrorComponent
        from ..models.api_v1_endpoints_create_archived_reason_error_component import (
            ApiV1EndpointsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_create_check_result_retention_days_error_component import (
            ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_check_results_error_component import (
            ApiV1EndpointsCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_created_by_component_error_component import (
            ApiV1EndpointsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_create_created_by_user_error_component import (
            ApiV1EndpointsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_create_criticality_error_component import (
            ApiV1EndpointsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_debug_mode_error_component import (
            ApiV1EndpointsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_create_discovery_enabled_error_component import (
            ApiV1EndpointsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_create_display_name_error_component import (
            ApiV1EndpointsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_create_do_not_monitor_error_component import (
            ApiV1EndpointsCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_create_k8s_app_error_component import ApiV1EndpointsCreateK8SAppErrorComponent
        from ..models.api_v1_endpoints_create_k8s_cluster_error_component import (
            ApiV1EndpointsCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_create_kind_error_component import ApiV1EndpointsCreateKindErrorComponent
        from ..models.api_v1_endpoints_create_labels_error_component import ApiV1EndpointsCreateLabelsErrorComponent
        from ..models.api_v1_endpoints_create_last_agent_metrics_error_component import (
            ApiV1EndpointsCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_loadbalancer_instance_error_component import (
            ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent,
        )
        from ..models.api_v1_endpoints_create_managed_by_content_type_error_component import (
            ApiV1EndpointsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_create_managed_by_object_id_error_component import (
            ApiV1EndpointsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_create_modified_by_user_error_component import (
            ApiV1EndpointsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_create_name_error_component import ApiV1EndpointsCreateNameErrorComponent
        from ..models.api_v1_endpoints_create_non_field_errors_error_component import (
            ApiV1EndpointsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_create_organization_id_error_component import (
            ApiV1EndpointsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_create_platform_service_error_component import (
            ApiV1EndpointsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_create_pop_endpoint_error_component import (
            ApiV1EndpointsCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_create_provider_error_component import ApiV1EndpointsCreateProviderErrorComponent
        from ..models.api_v1_endpoints_create_provider_id_error_component import (
            ApiV1EndpointsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_create_provider_reference_error_component import (
            ApiV1EndpointsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_create_region_error_component import ApiV1EndpointsCreateRegionErrorComponent
        from ..models.api_v1_endpoints_create_remote_address_error_component import (
            ApiV1EndpointsCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_create_remote_port_error_component import (
            ApiV1EndpointsCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_create_resolved_ip_error_component import (
            ApiV1EndpointsCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_create_s3_cluster_error_component import (
            ApiV1EndpointsCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_create_scope_error_component import ApiV1EndpointsCreateScopeErrorComponent
        from ..models.api_v1_endpoints_create_sla_availability_error_component import (
            ApiV1EndpointsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_sla_target_error_component import (
            ApiV1EndpointsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_create_sla_window_days_error_component import (
            ApiV1EndpointsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_availability_error_component import (
            ApiV1EndpointsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_target_error_component import (
            ApiV1EndpointsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_create_slo_window_days_error_component import (
            ApiV1EndpointsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_create_spec_error_component import ApiV1EndpointsCreateSpecErrorComponent
        from ..models.api_v1_endpoints_create_target_availability_error_component import (
            ApiV1EndpointsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_create_workspace_id_error_component import (
            ApiV1EndpointsCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsCreateActualAvailabilityErrorComponent
                | ApiV1EndpointsCreateAnnotationsErrorComponent
                | ApiV1EndpointsCreateArchivedAtErrorComponent
                | ApiV1EndpointsCreateArchivedByErrorComponent
                | ApiV1EndpointsCreateArchivedErrorComponent
                | ApiV1EndpointsCreateArchivedReasonErrorComponent
                | ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsCreateCheckResultsErrorComponent
                | ApiV1EndpointsCreateCreatedByComponentErrorComponent
                | ApiV1EndpointsCreateCreatedByUserErrorComponent
                | ApiV1EndpointsCreateCriticalityErrorComponent
                | ApiV1EndpointsCreateDebugModeErrorComponent
                | ApiV1EndpointsCreateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsCreateDisplayNameErrorComponent
                | ApiV1EndpointsCreateDoNotMonitorErrorComponent
                | ApiV1EndpointsCreateK8SAppErrorComponent
                | ApiV1EndpointsCreateK8SClusterErrorComponent
                | ApiV1EndpointsCreateKindErrorComponent
                | ApiV1EndpointsCreateLabelsErrorComponent
                | ApiV1EndpointsCreateLastAgentMetricsErrorComponent
                | ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsCreateManagedByContentTypeErrorComponent
                | ApiV1EndpointsCreateManagedByObjectIdErrorComponent
                | ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsCreateModifiedByUserErrorComponent
                | ApiV1EndpointsCreateNameErrorComponent
                | ApiV1EndpointsCreateNonFieldErrorsErrorComponent
                | ApiV1EndpointsCreateOrganizationIdErrorComponent
                | ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsCreatePlatformServiceErrorComponent
                | ApiV1EndpointsCreatePopEndpointErrorComponent
                | ApiV1EndpointsCreateProviderErrorComponent
                | ApiV1EndpointsCreateProviderIdErrorComponent
                | ApiV1EndpointsCreateProviderReferenceErrorComponent
                | ApiV1EndpointsCreateReconciliationEnabledErrorComponent
                | ApiV1EndpointsCreateRegionErrorComponent
                | ApiV1EndpointsCreateRemoteAddressErrorComponent
                | ApiV1EndpointsCreateRemotePortErrorComponent
                | ApiV1EndpointsCreateResolvedIpErrorComponent
                | ApiV1EndpointsCreateS3ClusterErrorComponent
                | ApiV1EndpointsCreateScopeErrorComponent
                | ApiV1EndpointsCreateSlaAvailabilityErrorComponent
                | ApiV1EndpointsCreateSlaTargetErrorComponent
                | ApiV1EndpointsCreateSlaWindowDaysErrorComponent
                | ApiV1EndpointsCreateSloAvailabilityErrorComponent
                | ApiV1EndpointsCreateSloTargetErrorComponent
                | ApiV1EndpointsCreateSloWindowDaysErrorComponent
                | ApiV1EndpointsCreateSpecErrorComponent
                | ApiV1EndpointsCreateTargetAvailabilityErrorComponent
                | ApiV1EndpointsCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_0 = (
                        ApiV1EndpointsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_1 = (
                        ApiV1EndpointsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_2 = (
                        ApiV1EndpointsCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_3 = (
                        ApiV1EndpointsCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_4 = (
                        ApiV1EndpointsCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_5 = (
                        ApiV1EndpointsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_6 = (
                        ApiV1EndpointsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_7 = (
                        ApiV1EndpointsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_8 = (
                        ApiV1EndpointsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_9 = (
                        ApiV1EndpointsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_10 = (
                        ApiV1EndpointsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_11 = (
                        ApiV1EndpointsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_12 = (
                        ApiV1EndpointsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_13 = (
                        ApiV1EndpointsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_14 = (
                        ApiV1EndpointsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_15 = (
                        ApiV1EndpointsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_16 = (
                        ApiV1EndpointsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_17 = (
                        ApiV1EndpointsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_18 = (
                        ApiV1EndpointsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_19 = (
                        ApiV1EndpointsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_20 = (
                        ApiV1EndpointsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_21 = (
                        ApiV1EndpointsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_22 = (
                        ApiV1EndpointsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_23 = (
                        ApiV1EndpointsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_24 = (
                        ApiV1EndpointsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_25 = (
                        ApiV1EndpointsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_26 = (
                        ApiV1EndpointsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_27 = (
                        ApiV1EndpointsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_28 = (
                        ApiV1EndpointsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_29 = (
                        ApiV1EndpointsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_30 = (
                        ApiV1EndpointsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_31 = (
                        ApiV1EndpointsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_32 = (
                        ApiV1EndpointsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_33 = (
                        ApiV1EndpointsCreateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_34 = (
                        ApiV1EndpointsCreateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_35 = (
                        ApiV1EndpointsCreateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_36 = (
                        ApiV1EndpointsCreateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_37 = (
                        ApiV1EndpointsCreatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_38 = (
                        ApiV1EndpointsCreateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_39 = (
                        ApiV1EndpointsCreateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_40 = (
                        ApiV1EndpointsCreateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_41 = (
                        ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_42 = (
                        ApiV1EndpointsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_43 = (
                        ApiV1EndpointsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_44 = (
                        ApiV1EndpointsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_45 = (
                        ApiV1EndpointsCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_46 = (
                        ApiV1EndpointsCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_47 = (
                        ApiV1EndpointsCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_48 = (
                        ApiV1EndpointsCreateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_create_error_type_49 = (
                        ApiV1EndpointsCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_create_error_type_50 = (
                    ApiV1EndpointsCreateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_create_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_create_validation_error.additional_properties = d
        return api_v1_endpoints_create_validation_error

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
